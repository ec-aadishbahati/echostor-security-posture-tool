import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.api import admin, assessment, auth, reports
from app.core.config import settings
from app.middleware.rate_limit import limiter

app = FastAPI(
    title="EchoStor Security Posture Assessment API",
    description="API for comprehensive security posture assessment tool",
    version="1.0.0",
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

os.makedirs("reports", exist_ok=True)

app.mount("/reports", StaticFiles(directory="reports"), name="reports")

app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(assessment.router, prefix="/api/assessment", tags=["assessment"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])


@limiter.exempt
@app.get("/")
async def root():
    return {"message": "EchoStor Security Posture Assessment API", "version": "1.0.0"}


@limiter.exempt
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
