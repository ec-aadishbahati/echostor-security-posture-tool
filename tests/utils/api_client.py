"""API client for testing"""
import requests
from typing import Optional, Dict, Any


class APIClient:
    """API client with authentication support"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.token: Optional[str] = None
        self.session = requests.Session()
    
    def register(self, email: str, password: str, full_name: str = "Test User") -> Dict[str, Any]:
        """Register a new user"""
        response = self.session.post(
            f"{self.base_url}/api/auth/register",
            json={
                "email": email,
                "password": password,
                "full_name": full_name
            }
        )
        response.raise_for_status()
        data = response.json()
        self.token = data.get("access_token")
        if self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})
        return data
    
    def login(self, email: str, password: str) -> Dict[str, Any]:
        """Login with existing user"""
        response = self.session.post(
            f"{self.base_url}/api/auth/login",
            data={
                "username": email,
                "password": password
            }
        )
        response.raise_for_status()
        data = response.json()
        self.token = data.get("access_token")
        if self.token:
            self.session.headers.update({"Authorization": f"Bearer {self.token}"})
        return data
    
    def get_structure(self) -> Dict[str, Any]:
        """Get assessment structure"""
        response = self.session.get(f"{self.base_url}/api/assessments/structure")
        response.raise_for_status()
        return response.json()
    
    def start_assessment(self) -> Dict[str, Any]:
        """Start a new assessment"""
        response = self.session.post(f"{self.base_url}/api/assessments/start")
        response.raise_for_status()
        return response.json()
    
    def get_current_assessment(self) -> Dict[str, Any]:
        """Get current assessment"""
        response = self.session.get(f"{self.base_url}/api/assessments/current")
        response.raise_for_status()
        return response.json()
    
    def submit_response(self, assessment_id: str, question_id: str, 
                       answer_value: Any, comment: Optional[str] = None) -> Dict[str, Any]:
        """Submit a response to a question"""
        payload = {
            "question_id": question_id,
            "answer_value": answer_value
        }
        if comment:
            payload["comment"] = comment
        
        response = self.session.post(
            f"{self.base_url}/api/assessments/{assessment_id}/responses",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    def save_progress(self, assessment_id: str) -> Dict[str, Any]:
        """Save assessment progress"""
        response = self.session.post(
            f"{self.base_url}/api/assessments/{assessment_id}/save"
        )
        response.raise_for_status()
        return response.json()
    
    def save_consultation(self, assessment_id: str, interested: bool, 
                         details: Optional[str] = None) -> Dict[str, Any]:
        """Save consultation interest"""
        payload = {
            "consultation_interest": interested
        }
        if interested and details:
            payload["consultation_details"] = details
        
        response = self.session.post(
            f"{self.base_url}/api/assessments/{assessment_id}/consultation",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    def complete_assessment(self, assessment_id: str) -> Dict[str, Any]:
        """Complete an assessment"""
        response = self.session.post(
            f"{self.base_url}/api/assessments/{assessment_id}/complete"
        )
        response.raise_for_status()
        return response.json()
    
    def get_reports(self, assessment_id: str) -> Dict[str, Any]:
        """Get reports for an assessment"""
        response = self.session.get(
            f"{self.base_url}/api/reports?assessment_id={assessment_id}"
        )
        response.raise_for_status()
        return response.json()
    
    def generate_report(self, assessment_id: str, report_type: str = "standard") -> Dict[str, Any]:
        """Generate a report"""
        response = self.session.post(
            f"{self.base_url}/api/reports/generate",
            json={
                "assessment_id": assessment_id,
                "report_type": report_type
            }
        )
        response.raise_for_status()
        return response.json()
    
    def download_report(self, report_id: str) -> bytes:
        """Download a report PDF"""
        response = self.session.get(
            f"{self.base_url}/api/reports/{report_id}/download"
        )
        response.raise_for_status()
        return response.content
    
    def logout(self):
        """Clear authentication"""
        self.token = None
        self.session.headers.pop("Authorization", None)
