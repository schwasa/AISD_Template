from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_joke_endpoint_returns_a_joke() -> None:
    response = client.get("/joke")

    assert response.status_code == 200
    assert response.json()["joke"]