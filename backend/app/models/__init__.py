from sqlalchemy.orm import relationship

from app.models.assessment import AdminAuditLog, Assessment, AssessmentResponse, Report
from app.models.user import User

User.assessments = relationship(
    "Assessment", back_populates="user", cascade="all, delete-orphan"
)

__all__ = ["User", "Assessment", "AssessmentResponse", "Report", "AdminAuditLog"]
