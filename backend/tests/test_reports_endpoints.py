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
    assert "items" in data
    assert isinstance(data["items"], list)
    assert len(data["items"]) >= 1


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


def test_duplicate_standard_report_prevention(
    client: TestClient, auth_token, completed_assessment
):
    """Test that attempting to create duplicate standard reports returns existing report."""
    with patch("app.api.reports.BackgroundTasks.add_task") as _mock_task:
        response1 = client.post(
            f"/api/reports/{completed_assessment.id}/generate",
            headers={"Authorization": f"Bearer {auth_token}"},
        )
        assert response1.status_code == 200
        data1 = response1.json()
        report_id_1 = data1["id"]

        response2 = client.post(
            f"/api/reports/{completed_assessment.id}/generate",
            headers={"Authorization": f"Bearer {auth_token}"},
        )
        assert response2.status_code == 200
        data2 = response2.json()
        report_id_2 = data2["id"]

        assert report_id_1 == report_id_2
        assert data2["report_type"] == "standard"


def test_duplicate_ai_report_prevention(
    client: TestClient, auth_token, completed_assessment
):
    """Test that attempting to create duplicate AI reports returns existing report."""
    response1 = client.post(
        f"/api/reports/{completed_assessment.id}/request-ai-report",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={"message": "First request"},
    )
    assert response1.status_code == 200
    data1 = response1.json()
    assert data1["status"] == "pending"

    response2 = client.post(
        f"/api/reports/{completed_assessment.id}/request-ai-report",
        headers={"Authorization": f"Bearer {auth_token}"},
        json={"message": "Second request"},
    )
    assert response2.status_code == 200
    data2 = response2.json()
    assert "already requested" in data2["message"].lower()
    assert data2["status"] == "pending"


def test_concurrent_report_generation_race_condition(
    client: TestClient, auth_token, completed_assessment, db_session
):
    """Test that concurrent report generation attempts don't create duplicates."""
    from app.models.assessment import Report

    with patch("app.api.reports.BackgroundTasks.add_task") as _mock_task:
        responses = []
        for _ in range(3):
            response = client.post(
                f"/api/reports/{completed_assessment.id}/generate",
                headers={"Authorization": f"Bearer {auth_token}"},
            )
            responses.append(response)

        for response in responses:
            assert response.status_code == 200

        reports = (
            db_session.query(Report)
            .filter(
                Report.assessment_id == completed_assessment.id,
                Report.report_type == "standard",
            )
            .all()
        )
        assert len(reports) == 1


def test_different_report_types_allowed(
    client: TestClient, auth_token, completed_assessment, db_session
):
    """Test that different report types (standard vs AI) can coexist for same assessment."""
    from app.models.assessment import Report

    with patch("app.api.reports.BackgroundTasks.add_task") as _mock_task:
        response1 = client.post(
            f"/api/reports/{completed_assessment.id}/generate",
            headers={"Authorization": f"Bearer {auth_token}"},
        )
        assert response1.status_code == 200

        response2 = client.post(
            f"/api/reports/{completed_assessment.id}/request-ai-report",
            headers={"Authorization": f"Bearer {auth_token}"},
            json={"message": "AI report request"},
        )
        assert response2.status_code == 200

        reports = (
            db_session.query(Report)
            .filter(Report.assessment_id == completed_assessment.id)
            .all()
        )
        assert len(reports) == 2
        report_types = {r.report_type for r in reports}
        assert report_types == {"standard", "ai_enhanced"}


def test_user_reports_ordered_by_requested_at(
    client: TestClient, auth_token, completed_assessment, db_session
):
    """Test that user reports are returned in descending order by requested_at."""
    from datetime import UTC, datetime, timedelta

    from app.models.assessment import Report

    base_time = datetime.now(UTC)
    reports_data = [
        {"offset_minutes": -60, "type": "standard"},  # 1 hour ago
        {"offset_minutes": -30, "type": "ai_enhanced"},  # 30 minutes ago
    ]

    for data in reports_data:
        report = Report(
            assessment_id=completed_assessment.id,
            report_type=data["type"],
            status="completed",
            requested_at=base_time + timedelta(minutes=data["offset_minutes"]),
        )
        db_session.add(report)
    db_session.commit()

    response = client.get(
        "/api/reports/user/reports", headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    items = data["items"]

    if len(items) >= 2:
        for i in range(len(items) - 1):
            current_time = datetime.fromisoformat(
                items[i]["requested_at"].replace("Z", "+00:00")
            )
            next_time = datetime.fromisoformat(
                items[i + 1]["requested_at"].replace("Z", "+00:00")
            )
            assert current_time >= next_time, "Reports should be ordered by requested_at DESC"


def test_admin_retry_failed_standard_report(
    client: TestClient, admin_token, completed_assessment, db_session
):
    """Test that admin can retry a failed standard report."""
    from app.models.assessment import Report

    failed_report = Report(
        assessment_id=completed_assessment.id,
        report_type="standard",
        status="failed",
    )
    db_session.add(failed_report)
    db_session.commit()
    db_session.refresh(failed_report)

    with patch("app.api.reports.BackgroundTasks.add_task") as _mock_task:
        response = client.post(
            f"/api/reports/admin/{failed_report.id}/retry-standard",
            headers={"Authorization": f"Bearer {admin_token}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "generating"
        assert data["report_type"] == "standard"


def test_admin_retry_non_failed_report_fails(
    client: TestClient, admin_token, completed_assessment, db_session
):
    """Test that admin cannot retry a report that hasn't failed."""
    from app.models.assessment import Report

    completed_report = Report(
        assessment_id=completed_assessment.id,
        report_type="standard",
        status="completed",
    )
    db_session.add(completed_report)
    db_session.commit()
    db_session.refresh(completed_report)

    response = client.post(
        f"/api/reports/admin/{completed_report.id}/retry-standard",
        headers={"Authorization": f"Bearer {admin_token}"},
    )
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
