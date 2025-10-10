import logging
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.api import admin, assessment, auth, health, reports
from app.core.config import settings
from app.middleware.rate_limit import limiter
from app.middleware.security_headers import SecurityHeadersMiddleware

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting application startup...")
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

os.makedirs("reports", exist_ok=True)

app.mount("/reports", StaticFiles(directory="reports"), name="reports")

app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(assessment.router, prefix="/api/assessment", tags=["assessment"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(health.router, tags=["health"])


@limiter.exempt
@app.get("/")
async def root():
    return {"message": "EchoStor Security Posture Assessment API", "version": "1.0.0"}
