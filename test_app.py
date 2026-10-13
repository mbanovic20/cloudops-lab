from fastapi.testclient import TestClient
from app import app, create_app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "CloudOps Lab is running!"
    }

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "timestamp" in response.json()

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "http_requests_total" in response.text

def test_error_endpoint_disabled_by_default():
    response = TestClient(create_app()).get("/test-error")
    assert response.status_code == 404

def test_error_endpoint_enabled():
    response = TestClient(create_app(enable_test_endpoints=True)).get("/test-error")
    assert response.status_code == 500
