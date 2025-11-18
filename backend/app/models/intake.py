import uuid

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from app.core.database import Base


class IntakeSession(Base):
    __tablename__ = "assessment_intake_sessions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), nullable=True)  # Nullable for anonymous sessions
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    user_profile_json = Column(JSONB, nullable=False)
    ai_raw_response_json = Column(JSONB, nullable=True)
    final_selected_section_ids = Column(JSONB, nullable=True)
    time_preference = Column(String(20), nullable=True)
    used_fallback = Column(Boolean, default=False, nullable=False)
