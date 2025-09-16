from datetime import datetime, timedelta
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app.core.database import get_write_db, get_read_db
from app.core.config import settings
from app.models.user import User
from app.models.assessment import Assessment, AssessmentResponse as AssessmentResponseModel
from app.schemas.assessment import (
    AssessmentCreate, AssessmentResponse, SaveProgressRequest,
    AssessmentResponseResponse, AssessmentStructure
)
from app.services.question_parser import load_assessment_structure
from app.api.auth import get_current_user

router = APIRouter()

@router.get("/structure", response_model=AssessmentStructure)
async def get_assessment_structure():
    """Get the complete assessment structure with all questions"""
    return load_assessment_structure()

@router.post("/start", response_model=AssessmentResponse)
async def start_assessment(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_write_db)
):
    """Start a new assessment for the current user"""
    
    if hasattr(current_user, 'email') and current_user.email == "testuser@assessment.com":
        existing_test_user = db.query(User).filter(User.id == current_user.id).first()
        if not existing_test_user:
            test_user_db = User(
                id=current_user.id,
                email=current_user.email,
                full_name=current_user.full_name,
                company_name=current_user.company_name,
                password_hash="$2b$12$dummy_hash_for_test_user_only",
                is_active=True
            )
            db.add(test_user_db)
            db.commit()
            db.refresh(test_user_db)
    
    existing_assessment = db.query(Assessment).filter(
        and_(
            Assessment.user_id == current_user.id,
            Assessment.status == "in_progress"
        )
    ).first()
    
    if existing_assessment:
        return AssessmentResponse.model_validate(existing_assessment)
    
    expires_at = datetime.utcnow() + timedelta(days=settings.ASSESSMENT_EXPIRY_DAYS)
    
    assessment = Assessment(
        user_id=current_user.id,
        status="in_progress",
        started_at=datetime.utcnow(),
        expires_at=expires_at,
        last_saved_at=datetime.utcnow(),
        progress_percentage=0.0
    )
    
    db.add(assessment)
    db.commit()
    db.refresh(assessment)
    
    return AssessmentResponse.model_validate(assessment)

@router.get("/current", response_model=AssessmentResponse)
async def get_current_assessment(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_write_db)
):
    """Get the current assessment for the user"""
    
    assessment = db.query(Assessment).filter(
        and_(
            Assessment.user_id == current_user.id,
            Assessment.status == "in_progress"
        )
    ).first()
    
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No active assessment found"
        )
    
    if assessment.expires_at and datetime.utcnow() > assessment.expires_at:
        assessment.status = "expired"
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail="Assessment has expired"
        )
    
    return AssessmentResponse.model_validate(assessment)

@router.get("/{assessment_id}/responses", response_model=List[AssessmentResponseResponse])
async def get_assessment_responses(
    assessment_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_read_db)
):
    """Get all responses for an assessment"""
    
    assessment = db.query(Assessment).filter(
        and_(
            Assessment.id == assessment_id,
            Assessment.user_id == current_user.id
        )
    ).first()
    
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found"
        )
    
    responses = db.query(AssessmentResponseModel).filter(
        AssessmentResponseModel.assessment_id == assessment_id
    ).all()
    
    return [AssessmentResponseResponse.model_validate(response) for response in responses]

@router.post("/{assessment_id}/save-progress")
async def save_assessment_progress(
    assessment_id: str,
    progress_data: SaveProgressRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_write_db)
):
    """Save assessment progress"""
    
    assessment = db.query(Assessment).filter(
        and_(
            Assessment.id == assessment_id,
            Assessment.user_id == current_user.id,
            Assessment.status == "in_progress"
        )
    ).first()
    
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found or not in progress"
        )
    
    if assessment.expires_at and datetime.utcnow() > assessment.expires_at:
        assessment.status = "expired"
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail="Assessment has expired"
        )
    
    for response_data in progress_data.responses:
        existing_response = db.query(AssessmentResponseModel).filter(
            and_(
                AssessmentResponseModel.assessment_id == assessment_id,
                AssessmentResponseModel.question_id == response_data.question_id
            )
        ).first()
        
        if existing_response:
            existing_response.answer_value = response_data.answer_value
            existing_response.updated_at = datetime.utcnow()
        else:
            new_response = AssessmentResponseModel(
                assessment_id=assessment_id,
                section_id=response_data.section_id,
                question_id=response_data.question_id,
                answer_value=response_data.answer_value
            )
            db.add(new_response)
    
    assessment.last_saved_at = datetime.utcnow()
    
    total_responses = db.query(AssessmentResponseModel).filter(
        AssessmentResponseModel.assessment_id == assessment_id
    ).count()
    
    structure = load_assessment_structure()
    total_questions = structure.total_questions
    
    if total_questions > 0:
        assessment.progress_percentage = (total_responses / total_questions) * 100
    
    db.commit()
    
    return {"message": "Progress saved successfully", "progress_percentage": assessment.progress_percentage}

@router.post("/{assessment_id}/complete")
async def complete_assessment(
    assessment_id: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_write_db)
):
    """Complete an assessment"""
    
    assessment = db.query(Assessment).filter(
        and_(
            Assessment.id == assessment_id,
            Assessment.user_id == current_user.id,
            Assessment.status == "in_progress"
        )
    ).first()
    
    if not assessment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Assessment not found or not in progress"
        )
    
    if assessment.expires_at and datetime.utcnow() > assessment.expires_at:
        assessment.status = "expired"
        db.commit()
        raise HTTPException(
            status_code=status.HTTP_410_GONE,
            detail="Assessment has expired"
        )
    
    assessment.status = "completed"
    assessment.completed_at = datetime.utcnow()
    assessment.progress_percentage = 100.0
    
    db.commit()
    
    return {"message": "Assessment completed successfully"}
