from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path
from typing import List


app = FastAPI(title="Retail ML API")


# =========================
# FEATURES DEL MODELO
# =========================
FEATURES = [
    "age",
    "income",
    "purchase_frequency",
    "avg_ticket",
    "recency_days",
    "online_ratio",
    "annual_spend_est",
    "activity_score",
    "digital_score",
    "customer_score",
]


# =========================
# MODELO
# =========================
project_root = Path(__file__).resolve().parents[1]
model_path = project_root / "outputs" / "models" / "retail_model.joblib"

model = joblib.load(model_path)


# =========================
# MODELOS DE DATOS
# =========================
class CustomerData(BaseModel):
    age: float
    income: float
    purchase_frequency: float
    avg_ticket: float
    recency_days: float
    online_ratio: float
    annual_spend_est: float
    activity_score: float
    digital_score: float
    customer_score: float


# =========================
# ROOT
# =========================
@app.get("/")
def root():
    return {"message": "Retail ML API running"}


# =========================
# PREDICCIÓN SIMPLE
# =========================
@app.post("/predict")
def predict(data: CustomerData):

    df = pd.DataFrame([data.dict()])

    prediction = model.predict(df[FEATURES])[0]

    return {"predicted_sales": float(prediction)}


# =========================
# PREDICCIÓN BATCH
# =========================
@app.post("/predict-batch")
def predict_batch(data: List[CustomerData]):

    if len(data) == 0:
        raise HTTPException(status_code=400, detail="Lista vacía")

    df = pd.DataFrame([d.dict() for d in data])

    preds = model.predict(df[FEATURES])

    return {
        "predictions": preds.tolist()
    }


