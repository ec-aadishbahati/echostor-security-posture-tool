import pytest
from fastapi.testclient import TestClient

def test_health_endpoint(client: TestClient):
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()

def test_root_endpoint(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200

def test_docs_endpoint(client: TestClient):
    response = client.get("/docs")
    assert response.status_code == 200
