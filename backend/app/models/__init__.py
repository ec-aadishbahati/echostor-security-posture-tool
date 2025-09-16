from app.models.user import User
from app.models.assessment import Assessment, AssessmentResponse, Report, AdminAuditLog

User.assessments = relationship("Assessment", back_populates="user", cascade="all, delete-orphan")

__all__ = ["User", "Assessment", "AssessmentResponse", "Report", "AdminAuditLog"]
