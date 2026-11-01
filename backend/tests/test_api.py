from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_info_discloses_phase():
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    assert response.json()["phase"] == "scaffold"
