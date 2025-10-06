import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel


class AssessmentBase(BaseModel):
    status: str | None = "in_progress"


class AssessmentCreate(AssessmentBase):
    pass


class AssessmentUpdate(BaseModel):
    status: str | None = None
    completed_at: datetime | None = None
    progress_percentage: float | None = None


class AssessmentResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    status: str
    started_at: datetime
    completed_at: datetime | None
    expires_at: datetime | None
    last_saved_at: datetime
    progress_percentage: float
    consultation_interest: bool = False
    consultation_details: str | None = None

    class Config:
        from_attributes = True


class AssessmentResponseCreate(BaseModel):
    section_id: str
    question_id: str
    answer_value: Any
    comment: str | None = None


class AssessmentResponseUpdate(BaseModel):
    answer_value: Any


class AssessmentResponseResponse(BaseModel):
    id: uuid.UUID
    assessment_id: uuid.UUID
    section_id: str
    question_id: str
    answer_value: Any
    comment: str | None = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SaveProgressRequest(BaseModel):
    responses: list[AssessmentResponseCreate]


class QuestionOption(BaseModel):
    value: str
    label: str
    description: str | None = None


class Question(BaseModel):
    id: str
    section_id: str
    text: str
    type: str  # yes_no, multiple_choice, multiple_select
    weight: int
    explanation: str
    options: list[QuestionOption]


class Section(BaseModel):
    id: str
    title: str
    description: str
    questions: list[Question]


class AssessmentStructure(BaseModel):
    sections: list[Section]
    total_questions: int
