from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    DATABASE_URL_WRITE: str = os.getenv("DATABASE_URL_WRITE", "")
    DATABASE_URL_READ: str = os.getenv("DATABASE_URL_READ", "")
    
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 24
    ADMIN_TOKEN_EXPIRE_HOURS: int = 8
    
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL", "aadish.bahati@echostor.com")
    ADMIN_PASSWORD_HASH: str = os.getenv("ADMIN_PASSWORD_HASH", "")
    
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "https://echostor-security-posture.vercel.app",
        "https://*.vercel.app"
    ]
    
    ASSESSMENT_EXPIRY_DAYS: int = 15
    AUTO_SAVE_INTERVAL_MINUTES: int = 10
    
    REPORTS_DIR: str = "reports"
    AI_REPORT_DELIVERY_DAYS: int = 5
    
    class Config:
        env_file = ".env"

settings = Settings()
