import os
import sys
from datetime import UTC, datetime, timedelta

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

TEST_DATABASE_URL = "sqlite:///./test.db"
os.environ.setdefault("DATABASE_URL_WRITE", TEST_DATABASE_URL)
os.environ.setdefault("DATABASE_URL_READ", TEST_DATABASE_URL)
os.environ.setdefault("JWT_SECRET_KEY", "test-secret-key-for-testing-only-not-secure")

from app.core.database import Base, get_read_db, get_write_db
from app.core.security import create_access_token, get_password_hash
from app.main import app
from app.models.assessment import Assessment, Report
from app.models.assessment import AssessmentResponse as AssessmentResponseModel
from app.models.user import User

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(db_session):
    def override_get_write_db():
        try:
            yield db_session
        finally:
            pass

    def override_get_read_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_write_db] = override_get_write_db
    app.dependency_overrides[get_read_db] = override_get_read_db

    yield TestClient(app)

    app.dependency_overrides.clear()


@pytest.fixture
def test_user(db_session):
    user = User(
        email="test@example.com",
        full_name="Test User",
        company_name="Test Company",
        password_hash=get_password_hash("testpassword123"),
        is_active=True,
        is_admin=False,
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


@pytest.fixture
def test_admin_user(db_session):
    admin = User(
        email="admin@example.com",
        full_name="Admin User",
        company_name="Test Company",
        password_hash=get_password_hash("adminpassword123"),
        is_active=True,
        is_admin=True,
    )
    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)
    return admin


@pytest.fixture
def auth_token(test_user):
    return create_access_token(
        data={"sub": test_user.email, "user_id": str(test_user.id), "is_admin": False}
    )


@pytest.fixture
def admin_token(test_admin_user):
    return create_access_token(
        data={
            "sub": test_admin_user.email,
            "user_id": str(test_admin_user.id),
            "is_admin": True,
        },
        is_admin=True,
    )


@pytest.fixture
def test_assessment(db_session, test_user):
    assessment = Assessment(
        user_id=test_user.id,
        status="in_progress",
        started_at=datetime.now(UTC),
        expires_at=datetime.now(UTC) + timedelta(days=15),
        progress_percentage=0.0,
    )
    db_session.add(assessment)
    db_session.commit()
    db_session.refresh(assessment)
    return assessment


@pytest.fixture
def completed_assessment(db_session, test_user):
    assessment = Assessment(
        user_id=test_user.id,
        status="completed",
        started_at=datetime.now(UTC) - timedelta(days=1),
        completed_at=datetime.now(UTC),
        expires_at=datetime.now(UTC) + timedelta(days=14),
        progress_percentage=100.0,
    )
    db_session.add(assessment)
    db_session.commit()
    db_session.refresh(assessment)
    return assessment


@pytest.fixture
def admin_completed_assessment(db_session, test_admin_user):
    assessment = Assessment(
        user_id=test_admin_user.id,
        status="completed",
        started_at=datetime.now(UTC) - timedelta(days=1),
        completed_at=datetime.now(UTC),
        expires_at=datetime.now(UTC) + timedelta(days=14),
        progress_percentage=100.0,
    )
    db_session.add(assessment)
    db_session.commit()
    db_session.refresh(assessment)
    return assessment


@pytest.fixture
def test_assessment_response(db_session, test_assessment):
    response = AssessmentResponseModel(
        assessment_id=test_assessment.id,
        section_id="access-control",
        question_id="ac-1",
        answer_value="yes",
        comment="Test comment",
    )
    db_session.add(response)
    db_session.commit()
    db_session.refresh(response)
    return response


@pytest.fixture
def test_report(db_session, completed_assessment):
    report = Report(
        assessment_id=completed_assessment.id, report_type="standard", status="pending"
    )
    db_session.add(report)
    db_session.commit()
    db_session.refresh(report)
    return report
