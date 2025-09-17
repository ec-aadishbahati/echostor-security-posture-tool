import os
import sys

import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

TEST_DATABASE_URL = "sqlite:///./test.db"
os.environ.setdefault("DATABASE_URL_WRITE", TEST_DATABASE_URL)
os.environ.setdefault("DATABASE_URL_READ", TEST_DATABASE_URL)

from app.main import app  # noqa: E402


@pytest.fixture
def client():
    return TestClient(app)
