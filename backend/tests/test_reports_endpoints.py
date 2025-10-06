from unittest.mock import patch

from fastapi.testclient import TestClient


def test_generate_standard_report(client: TestClient, auth_token, completed_assessment):
    with patch("app.api.reports.BackgroundTasks.add_task") as _mock_task:
        response = client.post(
            f"/api/reports/{completed_assessment.id}/generate",
            headers={"Authorization": f"Bearer {auth_token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert "id" in data
        assert data["status"] == "generating"
        assert data["report_type"] == "standard"


def test_generate_report_assessment_not_found(client: TestClient, auth_token):
    response = client.post(
        "/api/reports/nonexistent-id/generate",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 404


def test_generate_report_incomplete_assessment(
    client: TestClient, auth_token, test_assessment
):
    response = client.post(
        f"/api/reports/{test_assessment.id}/generate",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 404
    assert "not found or not completed" in response.json()["detail"].lower()


def test_request_ai_report(client: TestClient, auth_token, completed_assessment):
    with patch("app.api.reports.BackgroundTasks.add_task") as _mock_task:
        response = client.post(
            f"/api/reports/{completed_assessment.id}/request-ai-report",
            headers={"Authorization": f"Bearer {auth_token}"},
            json={
                "assessment_id": str(completed_assessment.id),
                "message": "Please generate AI report",
            },
        )
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert data["status"] == "pending"


def test_get_user_reports(client: TestClient, auth_token, test_report):
    response = client.get(
        "/api/reports/user/reports", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_report_status(client: TestClient, auth_token, test_report):
    response = client.get(
        f"/api/reports/{test_report.id}/status",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "pending"


def test_get_report_status_not_found(client: TestClient, auth_token):
    response = client.get(
        "/api/reports/nonexistent-id/status",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 404


def test_download_report_not_ready(client: TestClient, auth_token, test_report):
    response = client.get(
        f"/api/reports/{test_report.id}/download",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 404
    assert "not ready" in response.json()["detail"].lower()


def test_admin_generate_ai_report(
    client: TestClient, admin_token, db_session, completed_assessment
):
    from app.models.assessment import Report

    ai_report = Report(
        assessment_id=completed_assessment.id,
        report_type="ai_enhanced",
        status="pending",
    )
    db_session.add(ai_report)
    db_session.commit()
    db_session.refresh(ai_report)

    with patch("app.api.reports.BackgroundTasks.add_task") as _mock_task:
        response = client.post(
            f"/api/reports/admin/{ai_report.id}/generate-ai",
            headers={"Authorization": f"Bearer {admin_token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "generating"


def test_admin_generate_ai_report_unauthorized(
    client: TestClient, auth_token, test_report
):
    response = client.post(
        f"/api/reports/admin/{test_report.id}/generate-ai",
        headers={"Authorization": f"Bearer {auth_token}"},
    )
    assert response.status_code == 403


def test_admin_release_report(client: TestClient, admin_token, test_report, db_session):
    test_report.status = "completed"
    test_report.report_type = "ai_enhanced"
    db_session.commit()

    response = client.post(
        f"/api/reports/admin/{test_report.id}/release",
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
