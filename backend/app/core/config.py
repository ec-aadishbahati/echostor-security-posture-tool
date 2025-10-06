from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL_WRITE: str | None = None
    DATABASE_URL_READ: str | None = None

    JWT_SECRET_KEY: str | None = None
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 24
    ADMIN_TOKEN_EXPIRE_HOURS: int = 8

    OPENAI_API_KEY: str | None = None

    ADMIN_EMAIL: str = "aadish.bahati@echostor.com"
    ADMIN_PASSWORD_HASH: str | None = None

    ADMIN_LOGIN_USER: str | None = None
    ADMIN_LOGIN_PASSWORD: str | None = None

    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
        "https://echostor-security-posture-tool.vercel.app",
    ]

    ASSESSMENT_EXPIRY_DAYS: int = 15
    AUTO_SAVE_INTERVAL_MINUTES: int = 10

    REPORTS_DIR: str = "reports"
    AI_REPORT_DELIVERY_DAYS: int = 5
    REDIS_URL: str | None = None
    SENTRY_DSN: str | None = None
    SENTRY_ENVIRONMENT: str = "development"

    @model_validator(mode="after")
    def validate_required_settings(self):
        if not self.JWT_SECRET_KEY:
            raise ValueError(
                "JWT_SECRET_KEY environment variable must be set. "
                "Generate one with: openssl rand -hex 32"
            )
        if not self.DATABASE_URL_WRITE:
            raise ValueError(
                "DATABASE_URL_WRITE environment variable must be set. "
                "Example: postgresql://user:pass@host:5432/dbname"
            )
        if not self.DATABASE_URL_READ:
            self.DATABASE_URL_READ = self.DATABASE_URL_WRITE
        return self

    class Config:
        env_file = ".env"


settings = Settings()
