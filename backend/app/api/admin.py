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
from app.core.security import get_password_hash

router = APIRouter()

@router.get("/users", response_model=List[UserResponse])
async def get_all_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    search: Optional[str] = Query(None),
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
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
    
    return [UserResponse.model_validate(user) for user in users]

@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: str,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
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
    
    return UserResponse.model_validate(user)

@router.get("/users/{user_id}/assessments", response_model=List[AssessmentResponseSchema])
async def get_user_assessments(
    user_id: str,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
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
    
    return [AssessmentResponseSchema.model_validate(assessment) for assessment in assessments]

@router.get("/assessments", response_model=List[AssessmentResponseSchema])
async def get_all_assessments(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    status: Optional[str] = Query(None),
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
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
    
    return [AssessmentResponseSchema.model_validate(assessment) for assessment in assessments]

@router.get("/dashboard/stats")
async def get_dashboard_stats(
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
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

@router.get("/users-progress-summary")
async def get_users_progress_summary(
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
):
    """Get detailed progress summary for all users"""
    
    users_with_progress = db.query(User).outerjoin(Assessment).all()
    
    summary = []
    for user in users_with_progress:
        assessment = db.query(Assessment).filter(Assessment.user_id == user.id).order_by(desc(Assessment.created_at)).first()
        
        user_data = {
            "user_id": str(user.id),
            "full_name": user.full_name,
            "email": user.email,
            "company_name": user.company_name,
            "assessment_status": assessment.status if assessment else "not_started",
            "progress_percentage": float(assessment.progress_percentage) if assessment else 0.0,
            "last_activity": assessment.last_saved_at if assessment else user.created_at,
            "days_since_activity": (datetime.utcnow() - (assessment.last_saved_at if assessment else user.created_at)).days
        }
        summary.append(user_data)
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="view_users_progress",
        details={"user_count": len(summary)},
        db=db
    )
    
    return {"users_progress": summary}

@router.get("/reports", response_model=List[ReportResponse])
async def get_all_reports(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    report_type: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
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
    
    return [ReportResponse.model_validate(report) for report in reports]

@router.get("/alerts")
async def get_alerts(
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
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

@router.delete("/users/{user_id}")
async def delete_user(
    user_id: str,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
):
    """Delete a user and all associated data"""
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    assessments = db.query(Assessment).filter(Assessment.user_id == user_id).all()
    for assessment in assessments:
        db.query(AssessmentResponse).filter(AssessmentResponse.assessment_id == assessment.id).delete()
        db.query(Report).filter(Report.assessment_id == assessment.id).delete()
    db.query(Assessment).filter(Assessment.user_id == user_id).delete()
    
    db.delete(user)
    db.commit()
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="delete_user",
        target_user_id=user_id,
        db=db
    )
    
    return {"message": "User deleted successfully"}

@router.post("/users/{user_id}/reset-password")
async def reset_user_password(
    user_id: str,
    request: dict,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
):
    """Reset a user's password"""
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    new_password = request.get("new_password")
    if not new_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="New password is required"
        )
    
    user.password_hash = get_password_hash(new_password)
    db.commit()
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="reset_password",
        target_user_id=user_id,
        db=db
    )
    
    return {"message": "Password reset successfully"}

@router.post("/users/bulk-update-status")
async def bulk_update_user_status(
    request: dict,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
):
    """Bulk activate/deactivate users"""
    
    user_ids = request.get("user_ids", [])
    is_active = request.get("is_active", True)
    
    if not user_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No user IDs provided"
        )
    
    updated_count = db.query(User).filter(User.id.in_(user_ids)).update(
        {"is_active": is_active}, synchronize_session=False
    )
    db.commit()
    
    await log_admin_action(
        admin_email=current_admin["email"],
        action="bulk_update_status",
        details={"user_ids": user_ids, "is_active": is_active, "updated_count": updated_count},
        db=db
    )
    
    return {"message": f"Updated {updated_count} users", "updated_count": updated_count}

@router.post("/users/bulk-delete")
async def bulk_delete_users(
    request: dict,
    current_admin = Depends(get_current_admin_user),
    db: Session = Depends(get_write_db)
):
    """Bulk delete users and all associated data"""
    
    user_ids = request.get("user_ids", [])
    
    if not user_ids:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No user IDs provided"
        )
    
    try:
        # Let SQLAlchemy handle cascade deletion automatically
        # User.assessments relationship has cascade="all, delete-orphan"
        # Assessment foreign keys have ondelete="CASCADE"
        deleted_count = db.query(User).filter(User.id.in_(user_ids)).delete(synchronize_session=False)
        db.commit()
        
        await log_admin_action(
            admin_email=current_admin["email"],
            action="bulk_delete_users",
            details={"user_ids": user_ids, "deleted_count": deleted_count},
            db=db
        )
        
        return {"message": f"Deleted {deleted_count} users", "deleted_count": deleted_count}
        
    except Exception as e:
        db.rollback()
        # Log the specific error for debugging
        print(f"Bulk delete error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete users: {str(e)}"
        )

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
