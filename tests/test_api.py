"""API tests using FastAPI TestClient.

Add: /predict with a stub model (check the response shape) and the missing-model-file case (503).
"""
from fastapi.testclient import TestClient

from stockpred.api import app

client = TestClient(app)


def test_health() -> None:
    assert client.get("/health").json() == {"status": "ok"}
