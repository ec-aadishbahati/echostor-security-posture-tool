import io
import logging
import os
import uuid

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    HTTPException,
    Query,
    Request,
    status,
)
from fastapi.responses import Response, StreamingResponse
from sqlalchemy import and_, desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload
from starlette.background import BackgroundTask
from weasyprint import HTML

from app.api.auth import get_current_admin_user, get_current_user
from app.core.database import get_db
from app.models.assessment import Assessment, AssessmentResponse, Report
from app.schemas.report import (
    AdminReportResponse,
    AIReportRequest,
    UserReportResponse,
)
from app.schemas.user import CurrentUserResponse
from app.services.question_parser import (
    filter_structure_by_sections,
    load_assessment_structure,
)
from app.services.report_generator import (
    calculate_assessment_scores,
    generate_ai_report,
    generate_report_html,
    generate_standard_report,
)
from app.services.storage import get_storage_service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/{assessment_id}/generate", response_model=UserReportResponse)
async def generate_report(
    request: Request,
    assessment_id: str,
    background_tasks: BackgroundTasks,
    current_user: CurrentUserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Generate a standard PDF report for a completed assessment"""

    region = os.getenv("FLY_REGION")
    primary = os.getenv("FLY_PRIMARY_REGION", "iad")
    if region and primary and region != primary:
        return Response(status_code=409, headers={"fly-replay": f"region={primary}"})

    assessment = (
        db.query(Assessment)
        .filter(
            and_(
                Assessment.id == assessment_id,
                Assessment.user_id == current_user.id,
                Assessment.status == "completed",
            )
        )
        .first()
    )

    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found or not completed",
        )

    existing_report = (
        db.query(Report)
        .filter(
            and_(
                Report.assessment_id == assessment_id, Report.report_type == "standard"
            )
        )
        .first()
    )

    if existing_report:
        return UserReportResponse.model_validate(existing_report)

    report = Report(
        assessment_id=assessment_id, report_type="standard", status="generating"
    )

    db.add(report)
    try:
        db.commit()
        db.refresh(report)
        background_tasks.add_task(generate_standard_report, str(report.id))
    except IntegrityError:
        db.rollback()
        existing_report = (
            db.query(Report)
            .filter(
                and_(
                    Report.assessment_id == assessment_id,
                    Report.report_type == "standard",
                )
            )
            .first()
        )
        if existing_report:
            return UserReportResponse.model_validate(existing_report)
        raise

    return UserReportResponse.model_validate(report)


@router.post("/{assessment_id}/request-ai-report")
async def request_ai_report(
    request: Request,
    assessment_id: str,
    request_data: AIReportRequest,
    current_user: CurrentUserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Request an AI-enhanced report (admin will generate it)"""

    assessment = (
        db.query(Assessment)
        .filter(
            and_(
                Assessment.id == assessment_id,
                Assessment.user_id == current_user.id,
                Assessment.status == "completed",
            )
        )
        .first()
    )

    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found or not completed",
        )

    existing_report = (
        db.query(Report)
        .filter(
            and_(
                Report.assessment_id == assessment_id,
                Report.report_type == "ai_enhanced",
            )
        )
        .first()
    )

    if existing_report:
        return {
            "message": "AI report already requested",
            "status": existing_report.status,
            "estimated_delivery": "3-5 business days",
        }

    report = Report(
        assessment_id=assessment_id, report_type="ai_enhanced", status="pending"
    )

    db.add(report)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        existing_report = (
            db.query(Report)
            .filter(
                and_(
                    Report.assessment_id == assessment_id,
                    Report.report_type == "ai_enhanced",
                )
            )
            .first()
        )
        if existing_report:
            return {
                "message": "AI report already requested",
                "status": existing_report.status,
                "estimated_delivery": "3-5 business days",
            }
        raise

    return {
        "message": "AI report requested successfully",
        "status": "pending",
        "estimated_delivery": "3-5 business days",
    }


@router.post("/admin/{report_id}/generate-ai", response_model=AdminReportResponse)
async def admin_generate_ai_report(
    request: Request,
    report_id: str,
    background_tasks: BackgroundTasks,
    current_admin=Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Admin endpoint to generate AI-enhanced reports"""

    report = (
        db.query(Report)
        .filter(
            and_(
                Report.id == report_id,
                Report.report_type == "ai_enhanced",
                Report.status == "pending",
            )
        )
        .first()
    )

    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found or not pending",
        )

    report.status = "generating"
    db.commit()

    background_tasks.add_task(generate_ai_report, str(report.id))

    return AdminReportResponse.model_validate(report)


@router.post("/admin/{report_id}/retry-standard", response_model=AdminReportResponse)
async def admin_retry_standard_report(
    request: Request,
    report_id: str,
    background_tasks: BackgroundTasks,
    current_admin=Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Admin endpoint to retry generating a failed standard report"""

    region = os.getenv("FLY_REGION")
    primary = os.getenv("FLY_PRIMARY_REGION", "iad")
    if region and primary and region != primary:
        return Response(status_code=409, headers={"fly-replay": f"region={primary}"})

    report = (
        db.query(Report)
        .filter(
            and_(
                Report.id == report_id,
                Report.report_type == "standard",
                Report.status == "failed",
            )
        )
        .first()
    )

    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found or not in failed status",
        )

    report.status = "generating"
    report.file_path = None
    report.completed_at = None
    db.commit()

    background_tasks.add_task(generate_standard_report, str(report.id))

    return AdminReportResponse.model_validate(report)


@router.post("/admin/{report_id}/release")
async def admin_release_ai_report(
    request: Request,
    report_id: str,
    current_admin=Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Admin endpoint to release AI-enhanced reports to users"""

    report = (
        db.query(Report)
        .filter(
            and_(
                Report.id == report_id,
                Report.report_type == "ai_enhanced",
                Report.status == "completed",
            )
        )
        .first()
    )

    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found or not ready for release",
        )

    report.status = "released"
    db.commit()

    return {"message": "AI report released to user", "report_id": report_id}


@router.post("/admin/release-bulk")
async def admin_bulk_release_ai_reports(
    request: Request,
    report_ids: list[str],
    current_admin=Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Admin endpoint to bulk release multiple AI-enhanced reports"""

    if not report_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No report IDs provided",
        )

    reports = (
        db.query(Report)
        .filter(
            and_(
                Report.id.in_(report_ids),
                Report.report_type == "ai_enhanced",
                Report.status == "completed",
            )
        )
        .all()
    )

    if not reports:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No reports found ready for release",
        )

    released_count = 0
    released_ids = []
    skipped_ids = []

    for report in reports:
        if report.status == "completed":
            report.status = "released"
            released_count += 1
            released_ids.append(str(report.id))
        else:
            skipped_ids.append(str(report.id))

    db.commit()

    return {
        "message": f"Released {released_count} AI reports",
        "released_count": released_count,
        "released_ids": released_ids,
        "skipped_ids": skipped_ids,
    }


@router.get("/{report_id}/download")
async def download_report(
    request: Request,
    report_id: str,
    current_user: CurrentUserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Download a completed report"""

    region = os.getenv("FLY_REGION")
    primary = os.getenv("FLY_PRIMARY_REGION", "iad")
    if region and primary and region != primary:
        return Response(status_code=409, headers={"fly-replay": f"region={primary}"})

    report = db.query(Report).join(Assessment).filter(Report.id == report_id).first()

    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Report not found"
        )

    if not current_user.is_admin and report.assessment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied"
        )

    if report.status not in ["completed", "released"]:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not ready for download",
        )

    filename = f"security_assessment_report_{report.report_type}_{report_id}.pdf"
    storage_service = get_storage_service()

    file_exists = report.file_path and storage_service.exists(report.file_path)

    if not file_exists:
        logger.warning(
            f"Report file not found for report_id {report_id}, regenerating on-demand"
        )

        if report.report_type != "standard":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Report file not found and cannot be regenerated",
            )

        try:
            assessment = (
                db.query(Assessment).filter(Assessment.id == report.assessment_id).first()
            )
            if not assessment:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Assessment not found",
                )

            responses = (
                db.query(AssessmentResponse)
                .filter(AssessmentResponse.assessment_id == assessment.id)
                .all()
            )

            structure = load_assessment_structure()
            if assessment.selected_section_ids:
                structure = filter_structure_by_sections(
                    structure, assessment.selected_section_ids
                )

            scores = calculate_assessment_scores(responses, structure)
            html_content = generate_report_html(assessment, responses, scores, structure)

            pdf_bytes = HTML(string=html_content).write_pdf()

            new_filename = f"report_{report_id}_{uuid.uuid4().hex[:8]}.pdf"
            storage_location = storage_service.save(pdf_bytes, new_filename)
            report.file_path = storage_location
            db.commit()

            logger.info(
                f"Successfully regenerated report file for report_id {report_id}"
            )

            pdf_stream = io.BytesIO(pdf_bytes)
            headers = {
                "Content-Disposition": f'attachment; filename="{filename}"',
                "Content-Type": "application/pdf",
            }
            return StreamingResponse(
                pdf_stream,
                media_type="application/pdf",
                headers=headers,
            )

        except Exception as e:
            logger.error(
                f"Failed to regenerate report for report_id {report_id}: {str(e)}",
                exc_info=True,
            )
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to regenerate report file",
            )

    try:
        file_handle = storage_service.open(report.file_path)
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Report file not found"
        )

    if hasattr(file_handle, "seek"):
        file_handle.seek(0)

    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"',
        "Content-Type": "application/pdf",
    }

    background = None
    if hasattr(file_handle, "close"):
        background = BackgroundTask(file_handle.close)

    return StreamingResponse(
        file_handle,
        media_type="application/pdf",
        headers=headers,
        background=background,
    )


@router.get("/user/reports")
async def get_user_reports(
    request: Request,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    current_user: CurrentUserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get all reports for the current user with pagination"""

    query = (
        db.query(Report)
        .join(Assessment)
        .filter(Assessment.user_id == current_user.id)
        .options(joinedload(Report.assessment).joinedload(Assessment.user))
    )

    total = query.count()
    reports = query.order_by(desc(Report.requested_at)).offset(skip).limit(limit).all()

    from app.utils.pagination import paginate

    return paginate(
        items=[UserReportResponse.model_validate(report) for report in reports],
        total=total,
        skip=skip,
        limit=limit,
    )


@router.get("/{report_id}/status", response_model=UserReportResponse)
async def get_report_status(
    request: Request,
    report_id: str,
    current_user: CurrentUserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Get the status of a specific report"""

    report = db.query(Report).join(Assessment).filter(Report.id == report_id).first()

    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Report not found"
        )

    if not current_user.is_admin and report.assessment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied"
        )

    return UserReportResponse.model_validate(report)
