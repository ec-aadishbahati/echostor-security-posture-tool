from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str | None = None
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
    RATE_LIMIT_ENABLED: bool = True

    SENTRY_DSN: str | None = None
    SENTRY_ENVIRONMENT: str = "development"
    SENTRY_TRACES_SAMPLE_RATE: float = 1.0
    SENTRY_PROFILES_SAMPLE_RATE: float = 1.0

    @model_validator(mode="after")
    def validate_required_settings(self):
        if not self.JWT_SECRET_KEY:
            raise ValueError(
                "JWT_SECRET_KEY environment variable must be set. "
                "Generate one with: openssl rand -hex 32"
            )
        if not self.DATABASE_URL:
            if self.DATABASE_URL_WRITE:
                self.DATABASE_URL = self.DATABASE_URL_WRITE
            else:
                raise ValueError(
                    "DATABASE_URL environment variable must be set. "
                    "Example: postgresql://user:pass@host:5432/dbname"
                )
        return self

    class Config:
        env_file = ".env"


settings = Settings()
