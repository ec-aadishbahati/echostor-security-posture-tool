"""Test configuration"""
import os
from typing import Optional


class TestConfig:
    """Configuration for E2E tests"""
    
    API_BASE_URL = os.getenv("TEST_API_URL", "http://localhost:8000")
    FRONTEND_BASE_URL = os.getenv("TEST_FRONTEND_URL", "http://localhost:3000")
    
    TEST_EMAIL = os.getenv("TEST_EMAIL")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")
    
    HEADLESS = os.getenv("TEST_HEADLESS", "true").lower() == "true"
    SLOW_MO = int(os.getenv("TEST_SLOW_MO", "0"))  # Milliseconds to slow down operations
    SCREENSHOT_ON_FAILURE = os.getenv("TEST_SCREENSHOT", "true").lower() == "true"
    
    DEFAULT_TIMEOUT = int(os.getenv("TEST_TIMEOUT", "30000"))  # 30 seconds
    REPORT_GENERATION_TIMEOUT = int(os.getenv("TEST_REPORT_TIMEOUT", "120000"))  # 2 minutes
    
    CLEANUP_AFTER_TEST = os.getenv("TEST_CLEANUP", "true").lower() == "true"
    
    SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
    REPORTS_DIR = os.path.join(os.path.dirname(__file__), "test_reports")
    
    @classmethod
    def ensure_dirs(cls):
        """Ensure required directories exist"""
        os.makedirs(cls.SCREENSHOTS_DIR, exist_ok=True)
        os.makedirs(cls.REPORTS_DIR, exist_ok=True)
