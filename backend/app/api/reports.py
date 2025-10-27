import os

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    HTTPException,
    Query,
    Request,
    status,
)
from fastapi.responses import FileResponse
from sqlalchemy import and_, desc
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, joinedload

from app.api.auth import get_current_admin_user, get_current_user
from app.core.database import get_db
from app.models.assessment import Assessment, Report
from app.schemas.report import AIReportRequest, ReportResponse
from app.schemas.user import CurrentUserResponse
from app.services.report_generator import generate_ai_report, generate_standard_report

router = APIRouter()


@router.post("/{assessment_id}/generate", response_model=ReportResponse)
async def generate_report(
    request: Request,
    assessment_id: str,
    background_tasks: BackgroundTasks,
    current_user: CurrentUserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Generate a standard PDF report for a completed assessment"""

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
        return ReportResponse.model_validate(existing_report)

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
                    Report.assessment_id == assessment_id, Report.report_type == "standard"
                )
            )
            .first()
        )
        if existing_report:
            return ReportResponse.model_validate(existing_report)
        raise

    return ReportResponse.model_validate(report)


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


@router.post("/admin/{report_id}/generate-ai", response_model=ReportResponse)
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

    return ReportResponse.model_validate(report)


@router.post("/admin/{report_id}/retry-standard", response_model=ReportResponse)
async def admin_retry_standard_report(
    request: Request,
    report_id: str,
    background_tasks: BackgroundTasks,
    current_admin=Depends(get_current_admin_user),
    db: Session = Depends(get_db),
):
    """Admin endpoint to retry generating a failed standard report"""

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

    return ReportResponse.model_validate(report)


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


@router.get("/{report_id}/download")
async def download_report(
    request: Request,
    report_id: str,
    current_user: CurrentUserResponse = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Download a completed report"""

    report = db.query(Report).join(Assessment).filter(Report.id == report_id).first()

    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Report not found"
        )

    if not current_user.is_admin and report.assessment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Access denied"
        )

    if (report.status not in ["completed", "released"]) or not report.file_path:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not ready for download",
        )

    if not os.path.exists(report.file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Report file not found"
        )

    filename = f"security_assessment_report_{report.report_type}_{report_id}.pdf"
    return FileResponse(
        path=report.file_path, filename=filename, media_type="application/pdf"
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
        items=[ReportResponse.model_validate(report) for report in reports],
        total=total,
        skip=skip,
        limit=limit,
    )


@router.get("/{report_id}/status", response_model=ReportResponse)
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

    return ReportResponse.model_validate(report)
