"""Test user factory"""
import random
import string
from typing import Dict, Optional


class UserFactory:
    """Factory for creating test users"""
    
    @staticmethod
    def generate_email(prefix: str = "test") -> str:
        """Generate a unique test email"""
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"{prefix}_{random_suffix}@echostor-test.com"
    
    @staticmethod
    def generate_password(length: int = 12) -> str:
        """Generate a secure random password"""
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(random.choices(chars, k=length))
    
    @staticmethod
    def create_test_user(email: Optional[str] = None, 
                        password: Optional[str] = None,
                        full_name: Optional[str] = None) -> Dict[str, str]:
        """Create test user credentials"""
        return {
            "email": email or UserFactory.generate_email(),
            "password": password or UserFactory.generate_password(),
            "full_name": full_name or "Test User"
        }
