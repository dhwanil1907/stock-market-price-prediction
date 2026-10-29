"""Scoring API for MSFT.

Batch scoring from localhost. Don't call it "deployed" or "real-time" anywhere.
"""
from fastapi import FastAPI

app = FastAPI(title="MSFT Direction Predictor")

# Load outputs/model.joblib once at startup, not on every request.
# If the file is missing, /predict should return a clear 503, not a stack trace.


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/predict")
def predict() -> dict[str, float | str]:
    """Return {"ticker", "as_of", "p_up", "model"} for the latest available trading day.

    Steps:
    1. Read the cached bars (or refresh them), build features, take the last row.
    2. Run predict_proba and return the up-probability with the date it refers to.
    There is no ticker parameter, since the model is trained on MSFT only.
    Use a pydantic response model once the shape is settled.
    """
    raise NotImplementedError
