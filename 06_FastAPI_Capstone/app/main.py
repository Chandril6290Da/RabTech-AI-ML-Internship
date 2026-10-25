from contextlib import asynccontextmanager
from pathlib import Path
import os
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ConfigDict, Field

APP_DIR = Path(__file__).resolve().parent
REPO_ROOT = APP_DIR.parents[1]
MODEL_PATH = Path(os.getenv(
    "MODEL_PATH",
    str(REPO_ROOT / "models" / "customer_churn_preprocessing_pipeline.joblib")
))

FEATURE_COLUMNS = [
    "tenure_months",
    "support_tickets",
    "monthly_spend_inr",
    "last_login_days",
    "plan_type",
]

model = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    if not MODEL_PATH.is_file():
        raise RuntimeError(f"Model file not found: {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)
    yield
    model = None


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict customer churn using a saved scikit-learn pipeline.",
    version="1.0.0",
    lifespan=lifespan,
)


class CustomerFeatures(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tenure_months: int = Field(ge=0, le=1200)
    support_tickets: int = Field(ge=0, le=10000)
    monthly_spend_inr: float = Field(ge=0, le=1000000)
    last_login_days: int = Field(ge=0, le=100000)
    plan_type: Literal["Basic", "Pro", "Standard"]


class PredictionResponse(BaseModel):
    prediction: int
    prediction_label: Literal["not_churned", "churned"]
    probability_churn: float = Field(ge=0, le=1)
    probability_not_churn: float = Field(ge=0, le=1)
    model_name: str


@app.get("/")
def root():
    return {
        "service": "Customer Churn Prediction API",
        "health": "/health",
        "prediction": "POST /predict",
        "documentation": "/docs",
    }


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict", response_model=PredictionResponse)
def predict(customer: CustomerFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded.")

    input_df = pd.DataFrame(
        [customer.model_dump()],
        columns=FEATURE_COLUMNS,
    )

    try:
        prediction = int(model.predict(input_df)[0])

        if not hasattr(model, "predict_proba"):
            raise HTTPException(
                status_code=500,
                detail="Model does not support probability predictions.",
            )

        probabilities = model.predict_proba(input_df)[0]
        classes = list(model.classes_)

        probability_churn = float(probabilities[classes.index(1)])
        probability_not_churn = float(probabilities[classes.index(0)])

        return PredictionResponse(
            prediction=prediction,
            prediction_label="churned" if prediction == 1 else "not_churned",
            probability_churn=probability_churn,
            probability_not_churn=probability_not_churn,
            model_name="customer_churn_preprocessing_pipeline",
        )
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed. Check server logs.",
        ) from exc
