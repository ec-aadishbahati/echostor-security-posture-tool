from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import desc, func, and_
from datetime import datetime, timedelta

from app.core.database import get_read_db, get_write_db
from app.models.user import User
from app.models.assessment import Assessment, AssessmentResponse, Report, AdminAuditLog
from app.schemas.user import UserResponse
from app.schemas.assessment import AssessmentResponse as AssessmentResponseSchema
from app.schemas.report import ReportResponse
from app.api.auth import get_current_admin_user

router = APIRouter()

@router.get("/users", response_model=List[UserResponse])
async def get_all_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    search: Optional[str] = Query(None),
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_read_db)
):
    """Get all users with pagination and search"""
    
    query = db.query(User)
    
    if search:
        search_param = f"%{search}%"
        query = query.filter(
            User.full_name.ilike(search_param) |
            User.email.ilike(search_param) |
            User.company_name.ilike(search_param)
        )
    
    users = query.offset(skip).limit(limit).all()
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="view_users",
        details={"search": search, "count": len(users)},
        db=db
    )
    
    return [UserResponse.from_orm(user) for user in users]

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: str,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_read_db)
):
    """Get a specific user by ID"""
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="view_user",
        target_user_id=user_id,
        db=db
    )
    
    return UserResponse.from_orm(user)

@router.get("/users/{user_id}/assessments", response_model=List[AssessmentResponseSchema])
async def get_user_assessments(
    user_id: str,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_read_db)
):
    """Get all assessments for a specific user"""
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    assessments = db.query(Assessment).filter(
        Assessment.user_id == user_id
    ).order_by(desc(Assessment.created_at)).all()
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="view_user_assessments",
        target_user_id=user_id,
        details={"assessment_count": len(assessments)},
        db=db
    )
    
    return [AssessmentResponseSchema.from_orm(assessment) for assessment in assessments]

@router.get("/assessments", response_model=List[AssessmentResponseSchema])
async def get_all_assessments(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    status: Optional[str] = Query(None),
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_read_db)
):
    """Get all assessments with filtering"""
    
    query = db.query(Assessment).join(User)
    
    if status:
        query = query.filter(Assessment.status == status)
    
    assessments = query.order_by(desc(Assessment.created_at)).offset(skip).limit(limit).all()
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="view_assessments",
        details={"status_filter": status, "count": len(assessments)},
        db=db
    )
    
    return [AssessmentResponseSchema.from_orm(assessment) for assessment in assessments]

@router.get("/dashboard/stats")
async def get_dashboard_stats(
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_read_db)
):
    """Get dashboard statistics"""
    
    total_users = db.query(func.count(User.id)).scalar()
    
    active_assessments = db.query(func.count(Assessment.id)).filter(
        Assessment.status == "in_progress"
    ).scalar()
    
    completed_assessments = db.query(func.count(Assessment.id)).filter(
        Assessment.status == "completed"
    ).scalar()
    
    expired_assessments = db.query(func.count(Assessment.id)).filter(
        Assessment.status == "expired"
    ).scalar()
    
    week_ago = datetime.utcnow() - timedelta(days=7)
    new_users_this_week = db.query(func.count(User.id)).filter(
        User.created_at >= week_ago
    ).scalar()
    
    seven_days_ago = datetime.utcnow() - timedelta(days=7)
    stuck_assessments = db.query(func.count(Assessment.id)).filter(
        and_(
            Assessment.status == "in_progress",
            Assessment.last_saved_at < seven_days_ago
        )
    ).scalar()
    
    avg_completion_time = db.query(
        func.avg(
            func.extract('epoch', Assessment.completed_at - Assessment.started_at) / 3600
        )
    ).filter(Assessment.status == "completed").scalar()
    
    stats = {
        "total_users": total_users or 0,
        "active_assessments": active_assessments or 0,
        "completed_assessments": completed_assessments or 0,
        "expired_assessments": expired_assessments or 0,
        "new_users_this_week": new_users_this_week or 0,
        "stuck_assessments": stuck_assessments or 0,
        "average_completion_hours": round(avg_completion_time or 0, 2)
    }
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="view_dashboard",
        details=stats,
        db=db
    )
    
    return stats

@router.get("/reports", response_model=List[ReportResponse])
async def get_all_reports(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    report_type: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_read_db)
):
    """Get all reports with filtering"""
    
    query = db.query(Report).join(Assessment).join(User)
    
    if report_type:
        query = query.filter(Report.report_type == report_type)
    
    if status:
        query = query.filter(Report.status == status)
    
    reports = query.order_by(desc(Report.requested_at)).offset(skip).limit(limit).all()
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="view_reports",
        details={"type_filter": report_type, "status_filter": status, "count": len(reports)},
        db=db
    )
    
    return [ReportResponse.from_orm(report) for report in reports]

@router.get("/alerts")
async def get_alerts(
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_read_db)
):
    """Get system alerts for admin dashboard"""
    
    alerts = []
    
    seven_days_ago = datetime.utcnow() - timedelta(days=7)
    stuck_assessments = db.query(Assessment).filter(
        and_(
            Assessment.status == "in_progress",
            Assessment.last_saved_at < seven_days_ago
        )
    ).count()
    
    if stuck_assessments > 0:
        alerts.append({
            "type": "warning",
            "title": "Stuck Assessments",
            "message": f"{stuck_assessments} assessments haven't been updated in 7+ days",
            "count": stuck_assessments
        })
    
    tomorrow = datetime.utcnow() + timedelta(days=1)
    expiring_soon = db.query(Assessment).filter(
        and_(
            Assessment.status == "in_progress",
            Assessment.expires_at <= tomorrow
        )
    ).count()
    
    if expiring_soon > 0:
        alerts.append({
            "type": "info",
            "title": "Expiring Soon",
            "message": f"{expiring_soon} assessments expire within 24 hours",
            "count": expiring_soon
        })
    
    pending_ai_reports = db.query(Report).filter(
        and_(
            Report.report_type == "ai_enhanced",
            Report.status == "pending"
        )
    ).count()
    
    if pending_ai_reports > 0:
        alerts.append({
            "type": "info",
            "title": "Pending AI Reports",
            "message": f"{pending_ai_reports} AI reports are pending generation",
            "count": pending_ai_reports
        })
    
    return {"alerts": alerts}

async def log_admin_action(
    admin_email: str,
    action: str,
    target_user_id: Optional[str] = None,
    details: Optional[dict] = None,
    db: Session = None
):
    """Log admin actions for audit trail"""
    
    if not db:
        return
    
    try:
        audit_log = AdminAuditLog(
            admin_email=admin_email,
            action=action,
            target_user_id=target_user_id,
            details=details or {}
        )
        
        db.add(audit_log)
        db.commit()
    except Exception as e:
        print(f"Error logging admin action: {e}")
        db.rollback()
