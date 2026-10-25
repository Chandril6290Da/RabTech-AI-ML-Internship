import sys
from pathlib import Path

CAPSTONE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(CAPSTONE_DIR))

from fastapi.testclient import TestClient
from app.main import app

VALID_PAYLOAD = {
    "tenure_months": 12,
    "support_tickets": 2,
    "monthly_spend_inr": 1499.0,
    "last_login_days": 7,
    "plan_type": "Standard",
}


def test_root():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json()["documentation"] == "/docs"


def test_health_and_model_loaded():
    with TestClient(app) as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok", "model_loaded": True}


def test_prediction_schema_and_probabilities():
    with TestClient(app) as client:
        response = client.post("/predict", json=VALID_PAYLOAD)

    assert response.status_code == 200
    body = response.json()
    assert body["prediction"] in (0, 1)
    assert body["prediction_label"] in ("not_churned", "churned")
    assert 0 <= body["probability_churn"] <= 1
    assert 0 <= body["probability_not_churn"] <= 1
    assert abs(
        body["probability_churn"] + body["probability_not_churn"] - 1
    ) < 1e-6
    assert body["prediction_label"] == (
        "churned" if body["prediction"] == 1 else "not_churned"
    )


def test_missing_field_returns_422():
    payload = VALID_PAYLOAD.copy()
    payload.pop("plan_type")
    with TestClient(app) as client:
        response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_invalid_plan_returns_422():
    payload = VALID_PAYLOAD.copy()
    payload["plan_type"] = "Premium"
    with TestClient(app) as client:
        response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_negative_tenure_returns_422():
    payload = VALID_PAYLOAD.copy()
    payload["tenure_months"] = -1
    with TestClient(app) as client:
        response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_unexpected_field_returns_422():
    payload = VALID_PAYLOAD.copy()
    payload["customer_id"] = "C001"
    with TestClient(app) as client:
        response = client.post("/predict", json=payload)
    assert response.status_code == 422
