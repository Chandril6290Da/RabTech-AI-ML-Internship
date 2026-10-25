FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV MODEL_PATH=/app/model.joblib

WORKDIR /app

COPY 06_FastAPI_Capstone/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY 06_FastAPI_Capstone/app ./app
COPY models/customer_churn_preprocessing_pipeline.joblib ./model.joblib

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
