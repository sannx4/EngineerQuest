from collections.abc import Iterator
from unittest.mock import patch

import pytest
from engineerquest_api.main import app, dependencies_ready
from fastapi.testclient import TestClient


@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(app) as client:
        yield client


def test_liveness_does_not_require_services(client: TestClient) -> None:
    assert client.get("/health/live").json() == {"status": "alive"}


@pytest.mark.parametrize("healthy,code", [(True, 200), (False, 503)])
def test_readiness_reports_dependency_state(
    client: TestClient, healthy: bool, code: int
) -> None:
    with patch("engineerquest_api.main.dependencies_ready", return_value=healthy):
        response = client.get("/health/ready")
    assert response.status_code == code
    assert response.json() == {"status": "ready" if healthy else "unavailable"}


def test_missing_config_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("DATABASE_URL", raising=False)
    assert dependencies_ready() is False


def test_driver_failure_is_not_exposed(client: TestClient) -> None:
    with patch.dict("os.environ", {"DATABASE_URL": "invalid-secret"}):
        response = client.get("/health/ready")
    assert response.status_code == 503
    assert "invalid-secret" not in response.text
