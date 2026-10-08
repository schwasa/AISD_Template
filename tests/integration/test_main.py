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


def test_categories_endpoint_returns_supported_categories() -> None:
    response = client.get("/categories")

    assert response.status_code == 200
    assert response.json() == {
        "categories": ["classic", "programming", "school"]
    }


def test_joke_endpoint_filters_by_category() -> None:
    response = client.get("/joke?category=programming")

    assert response.status_code == 200
    assert response.json()["category"] == "programming"


def test_joke_endpoint_rejects_unknown_category() -> None:
    response = client.get("/joke?category=unknown")

    assert response.status_code == 404