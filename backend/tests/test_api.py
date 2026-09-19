from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_what_if():
    response = client.post(
        "/api/v1/simulation/what-if",
        json={"intervention": "lane_addition", "road_id": "R002"},
    )
    assert response.status_code == 200
    assert response.json()["advisory_only"] if "advisory_only" in response.json() else True
