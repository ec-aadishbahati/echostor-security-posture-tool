from sqlalchemy import Column, String, DateTime, UUID, ForeignKey, DECIMAL, Text, Boolean, JSON
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship
import uuid

from app.core.database import Base

class Assessment(Base):
    __tablename__ = "assessments"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(50), default="in_progress")  # in_progress, completed, expired
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True))
    expires_at = Column(DateTime(timezone=True))
    last_saved_at = Column(DateTime(timezone=True), server_default=func.now())
    progress_percentage = Column(DECIMAL(5, 2), default=0.00)
    consultation_interest = Column(Boolean, default=False)
    consultation_details = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="assessments")
    responses = relationship("AssessmentResponse", back_populates="assessment", cascade="all, delete-orphan")
    reports = relationship("Report", back_populates="assessment", cascade="all, delete-orphan")

class AssessmentResponse(Base):
    __tablename__ = "assessment_responses"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    assessment_id = Column(String(36), ForeignKey("assessments.id", ondelete="CASCADE"), nullable=False)
    section_id = Column(String(50), nullable=False)
    question_id = Column(String(50), nullable=False)
    answer_value = Column(JSON)
    comment = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    assessment = relationship("Assessment", back_populates="responses")

    __table_args__ = (
        {"schema": None},
    )

class Report(Base):
    __tablename__ = "reports"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    assessment_id = Column(String(36), ForeignKey("assessments.id", ondelete="CASCADE"), nullable=False)
    report_type = Column(String(50), default="standard")  # standard, ai_enhanced
    file_path = Column(String(500))
    status = Column(String(50), default="pending")  # pending, generating, completed, failed
    requested_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True))

    assessment = relationship("Assessment", back_populates="reports")

class AdminAuditLog(Base):
    __tablename__ = "admin_audit_log"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    admin_email = Column(String(255))
    action = Column(String(100))
    target_user_id = Column(String(36))
    details = Column(JSON)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
