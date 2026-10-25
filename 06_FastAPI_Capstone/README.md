# Customer Churn Prediction API — Task 06

## Overview

A FastAPI REST service that serves a saved scikit-learn customer churn
preprocessing and classification pipeline.

## Architecture

Client JSON request
-> Pydantic validation
-> Pandas DataFrame with named features
-> Saved scikit-learn pipeline
-> Prediction and class probabilities
-> JSON response

The pipeline contains numeric imputation/scaling, categorical
imputation/one-hot encoding, and a Random Forest classifier.

## Endpoint

`POST /predict`

Example request:

```json
{
  "tenure_months": 12,
  "support_tickets": 2,
  "monthly_spend_inr": 1499.0,
  "last_login_days": 7,
  "plan_type": "Standard"
}
```

Allowed plan types: `Basic`, `Pro`, `Standard`.

Response fields:
- `prediction`: 0 = not churned; 1 = churned
- `prediction_label`: readable predicted class
- `probability_churn`: model-estimated probability of churn
- `probability_not_churn`: model-estimated probability of not churning
- `model_name`: saved pipeline identifier

## Local setup (PowerShell)

Run from the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r .\06_FastAPI_Capstone\requirements.txt
py -m uvicorn app.main:app --app-dir .\06_FastAPI_Capstone --reload
```

Interactive API docs: http://127.0.0.1:8000/docs
Health check: http://127.0.0.1:8000/health

If PowerShell blocks activation, run
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
in that terminal, then activate the environment again.

## Tests

```powershell
py -m pytest .\06_FastAPI_Capstone\tests -v
```

Tests check routes, model loading, prediction schema, probability
consistency, missing fields, invalid plan types, negative tenure,
and unexpected fields.

## Docker

Run from the repository root:

```powershell
docker build -f .\06_FastAPI_Capstone\Dockerfile -t customer-churn-api .
docker run --rm -p 8000:8000 customer-churn-api
```

Then visit http://127.0.0.1:8000/docs.

## Routes

| Method | Path | Purpose |
|---|---|---|
| GET | `/` | Service information |
| GET | `/health` | Health and model-loaded status |
| POST | `/predict` | Churn prediction |
| GET | `/docs` | Interactive Swagger documentation |

## Limitations and responsible use

The source churn dataset contains only 12 records. This is too small
to establish reliable real-world predictive performance. This API is
an internship demonstration, not a validated production decision system.
Use a larger, representative dataset and further evaluation before
real deployment. Public deployments also require suitable authentication,
monitoring, rate limiting, privacy controls, and data governance.

Only load trusted joblib model files. Confirm the scikit-learn version
used to create the artifact is compatible with the pinned runtime version.
