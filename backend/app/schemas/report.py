from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid

class ReportBase(BaseModel):
    report_type: str = "standard"

class ReportCreate(ReportBase):
    assessment_id: uuid.UUID

class ReportUpdate(BaseModel):
    status: Optional[str] = None
    file_path: Optional[str] = None
    completed_at: Optional[datetime] = None

class ReportResponse(BaseModel):
    id: uuid.UUID
    assessment_id: uuid.UUID
    report_type: str
    file_path: Optional[str]
    status: str
    requested_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True

class AIReportRequest(BaseModel):
    assessment_id: uuid.UUID
    message: Optional[str] = None
