import uuid
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, Field


class ReportBase(BaseModel):
    report_type: Annotated[str, Field(pattern="^(standard|ai_enhanced)$")] = "standard"


class ReportCreate(ReportBase):
    assessment_id: uuid.UUID


class ReportUpdate(BaseModel):
    status: (
        Annotated[
            str, Field(pattern="^(generating|completed|failed|pending|released)$")
        ]
        | None
    ) = None
    file_path: Annotated[str, Field(max_length=500)] | None = None
    completed_at: datetime | None = None


class MinimalUserResponse(BaseModel):
    id: uuid.UUID
    email: str
    full_name: str
    company_name: str

    class Config:
        from_attributes = True


class MinimalAssessmentResponse(BaseModel):
    id: uuid.UUID
    status: str
    completed_at: datetime | None
    user: MinimalUserResponse | None = None

    class Config:
        from_attributes = True


class ReportResponse(BaseModel):
    id: uuid.UUID
    assessment_id: uuid.UUID
    report_type: str
    file_path: str | None  # Internal use only, use download endpoint for access
    status: str
    requested_at: datetime
    completed_at: datetime | None
    assessment: MinimalAssessmentResponse | None = None

    class Config:
        from_attributes = True


class AIReportRequest(BaseModel):
    message: Annotated[str, Field(max_length=2000)] | None = None
