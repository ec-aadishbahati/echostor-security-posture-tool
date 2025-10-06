import uuid
from datetime import datetime

from pydantic import BaseModel


class ReportBase(BaseModel):
    report_type: str = "standard"


class ReportCreate(ReportBase):
    assessment_id: uuid.UUID


class ReportUpdate(BaseModel):
    status: str | None = None
    file_path: str | None = None
    completed_at: datetime | None = None


class ReportResponse(BaseModel):
    id: uuid.UUID
    assessment_id: uuid.UUID
    report_type: str
    file_path: str | None
    status: str
    requested_at: datetime
    completed_at: datetime | None

    class Config:
        from_attributes = True


class AIReportRequest(BaseModel):
    assessment_id: uuid.UUID
    message: str | None = None
