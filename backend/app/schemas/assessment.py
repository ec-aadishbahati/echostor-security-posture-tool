from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
import uuid

class AssessmentBase(BaseModel):
    status: Optional[str] = "in_progress"

class AssessmentCreate(AssessmentBase):
    pass

class AssessmentUpdate(BaseModel):
    status: Optional[str] = None
    completed_at: Optional[datetime] = None
    progress_percentage: Optional[float] = None

class AssessmentResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    status: str
    started_at: datetime
    completed_at: Optional[datetime]
    expires_at: Optional[datetime]
    last_saved_at: datetime
    progress_percentage: float
    consultation_interest: bool = False
    consultation_details: Optional[str] = None

    class Config:
        from_attributes = True

class AssessmentResponseCreate(BaseModel):
    section_id: str
    question_id: str
    answer_value: Any
    comment: Optional[str] = None

class AssessmentResponseUpdate(BaseModel):
    answer_value: Any

class AssessmentResponseResponse(BaseModel):
    id: uuid.UUID
    assessment_id: uuid.UUID
    section_id: str
    question_id: str
    answer_value: Any
    comment: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class SaveProgressRequest(BaseModel):
    responses: List[AssessmentResponseCreate]

class QuestionOption(BaseModel):
    value: str
    label: str
    description: Optional[str] = None

class Question(BaseModel):
    id: str
    section_id: str
    text: str
    type: str  # yes_no, multiple_choice, multiple_select
    weight: int
    explanation: str
    options: List[QuestionOption]

class Section(BaseModel):
    id: str
    title: str
    description: str
    questions: List[Question]

class AssessmentStructure(BaseModel):
    sections: List[Section]
    total_questions: int
