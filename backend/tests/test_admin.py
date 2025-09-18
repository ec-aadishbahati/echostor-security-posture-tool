import pytest
from fastapi.testclient import TestClient

def test_admin_users_endpoint_requires_auth(client: TestClient):
    response = client.get("/api/admin/users")
    assert response.status_code in [401, 403]
