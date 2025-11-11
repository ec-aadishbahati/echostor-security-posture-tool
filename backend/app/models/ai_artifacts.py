import uuid

from sqlalchemy import Column, DateTime, ForeignKey, Index, String, Text
from sqlalchemy.sql import func

from app.core.database import Base
from app.db.types import JSONBCompat


class AISectionArtifact(Base):
    """Stores structured JSON artifacts from AI section analysis"""

    __tablename__ = "ai_section_artifacts"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    report_id = Column(
        String(36), ForeignKey("reports.id", ondelete="CASCADE"), nullable=False
    )
    section_id = Column(String(100), nullable=False)
    artifact_json = Column(JSONBCompat, nullable=False)
    storage_uri = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    __table_args__ = (
        Index("idx_artifacts_report", "report_id"),
        Index("idx_artifacts_report_section", "report_id", "section_id", unique=True),
    )
