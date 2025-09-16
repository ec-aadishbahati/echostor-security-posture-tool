from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import and_
import os

from app.core.database import get_write_db, get_read_db
from app.models.user import User
from app.models.assessment import Assessment, Report
from app.schemas.report import ReportResponse, AIReportRequest
from app.services.report_generator import generate_standard_report, generate_ai_report
from app.api.auth import get_current_user, get_current_admin_user

router = APIRouter()

@router.post("/{assessment_id}/generate", response_model=ReportResponse)
async def generate_report(
    assessment_id: str,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_write_db)
):
    """Generate a standard PDF report for a completed assessment"""
    
    assessment = db.query(Assessment).filter(
        and_(
            Assessment.id == assessment_id,
            Assessment.user_id == current_user.id,
            Assessment.status == "completed"
        )
    ).first()
    
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found or not completed"
        )
    
    existing_report = db.query(Report).filter(
        and_(
            Report.assessment_id == assessment_id,
            Report.report_type == "standard"
        )
    ).first()
    
    if existing_report:
        return ReportResponse.from_orm(existing_report)
    
    report = Report(
        assessment_id=assessment_id,
        report_type="standard",
        status="generating"
    )
    
    db.add(report)
    db.commit()
    db.refresh(report)
    
    background_tasks.add_task(generate_standard_report, str(report.id))
    
    return ReportResponse.from_orm(report)

@router.post("/{assessment_id}/request-ai-report")
async def request_ai_report(
    assessment_id: str,
    request_data: AIReportRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_write_db)
):
    """Request an AI-enhanced report (admin will generate it)"""
    
    assessment = db.query(Assessment).filter(
        and_(
            Assessment.id == assessment_id,
            Assessment.user_id == current_user.id,
            Assessment.status == "completed"
        )
    ).first()
    
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found or not completed"
        )
    
    existing_report = db.query(Report).filter(
        and_(
            Report.assessment_id == assessment_id,
            Report.report_type == "ai_enhanced"
        )
    ).first()
    
    if existing_report:
        return {
            "message": "AI report already requested",
            "status": existing_report.status,
            "estimated_delivery": "3-5 business days"
        }
    
    report = Report(
        assessment_id=assessment_id,
        report_type="ai_enhanced",
        status="pending"
    )
    
    db.add(report)
    db.commit()
    
    return {
        "message": "AI report requested successfully",
        "status": "pending",
        "estimated_delivery": "3-5 business days"
    }

@router.post("/admin/{report_id}/generate-ai", response_model=ReportResponse)
async def admin_generate_ai_report(
    report_id: str,
    background_tasks: BackgroundTasks,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
):
    """Admin endpoint to generate AI-enhanced reports"""
    
    report = db.query(Report).filter(
        and_(
            Report.id == report_id,
            Report.report_type == "ai_enhanced",
            Report.status == "pending"
        )
    ).first()
    
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found or not pending"
        )
    
    report.status = "generating"
    db.commit()
    
    background_tasks.add_task(generate_ai_report, str(report.id))
    
    return ReportResponse.from_orm(report)

@router.get("/{report_id}/download")
async def download_report(
    report_id: str,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_read_db)
):
    """Download a completed report"""
    
    report = db.query(Report).join(Assessment).filter(Report.id == report_id).first()
    
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    
    is_admin = isinstance(current_user, dict) and current_user.get("is_admin")
    if not is_admin and report.assessment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )
    
    if report.status != "completed" or not report.file_path:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not ready for download"
        )
    
    if not os.path.exists(report.file_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report file not found"
        )
    
    filename = f"security_assessment_report_{report.report_type}_{report_id}.pdf"
    return FileResponse(
        path=report.file_path,
        filename=filename,
        media_type="application/pdf"
    )

@router.get("/user/reports", response_model=List[ReportResponse])
async def get_user_reports(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_read_db)
):
    """Get all reports for the current user"""
    
    reports = db.query(Report).join(Assessment).filter(
        Assessment.user_id == current_user.id
    ).all()
    
    return [ReportResponse.from_orm(report) for report in reports]

@router.get("/{report_id}/status", response_model=ReportResponse)
async def get_report_status(
    report_id: str,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_read_db)
):
    """Get the status of a specific report"""
    
    report = db.query(Report).join(Assessment).filter(Report.id == report_id).first()
    
    if not report:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found"
        )
    
    is_admin = isinstance(current_user, dict) and current_user.get("is_admin")
    if not is_admin and report.assessment.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied"
        )
    
    return ReportResponse.from_orm(report)
