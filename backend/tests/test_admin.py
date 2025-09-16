import pytest
from fastapi.testclient import TestClient

def test_admin_endpoints_exist(client: TestClient):
    response = client.get("/admin/")
    assert response.status_code in [200, 401, 422]
