import logging
from contextlib import asynccontextmanager

import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.api import admin, assessment, auth, health, openai_keys, reports
from app.core.config import settings
from app.middleware.performance import PerformanceMiddleware
from app.middleware.rate_limit import limiter
from app.middleware.security_headers import SecurityHeadersMiddleware

logger = logging.getLogger(__name__)

if settings.SENTRY_DSN:
    sentry_sdk.init(
        dsn=settings.SENTRY_DSN,
        environment=settings.SENTRY_ENVIRONMENT,
        traces_sample_rate=settings.SENTRY_TRACES_SAMPLE_RATE,
        profiles_sample_rate=settings.SENTRY_PROFILES_SAMPLE_RATE,
        enable_tracing=True,
        integrations=[
            sentry_sdk.integrations.fastapi.FastApiIntegration(),
            sentry_sdk.integrations.sqlalchemy.SqlalchemyIntegration(),
        ],
    )
    logger.info("Sentry performance monitoring initialized")
else:
    logger.warning("Sentry DSN not configured, performance monitoring disabled")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application startup...")

    import os

    try:
        os.makedirs(settings.REPORTS_DIR, exist_ok=True)
        logger.info(f"Reports directory ensured at: {settings.REPORTS_DIR}")
    except Exception as e:
        logger.error(f"Failed to create reports directory: {e}")

    logger.info("Starting cache warming...")
    try:
        from app.services.question_parser import load_assessment_structure_cached

        load_assessment_structure_cached()
        logger.info("Cache warming completed")
    except Exception as e:
        logger.error(f"Cache warming failed: {e}")

    yield


app = FastAPI(
    title="EchoStor Security Posture Assessment API",
    description="API for comprehensive security posture assessment tool",
    version="1.0.0",
    lifespan=lifespan,
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(PerformanceMiddleware)

app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(assessment.router, prefix="/api/assessment", tags=["assessment"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(openai_keys.router, prefix="/api/admin/openai-keys", tags=["admin"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(health.router, tags=["health"])


@limiter.exempt
@app.get("/")
async def root():
    return {"message": "EchoStor Security Posture Assessment API", "version": "1.0.0"}
