from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load model and feature names
model = joblib.load('logistic_pipeline.pkl')
model_columns = joblib.load('model_columns.pkl')

@app.get("/")
def home():
    return {"message": "Logistic Regression API is running. Visit /docs to test the model."}

@app.post("/predict")
def predict(data: dict):
    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Align with training columns
    df = df.reindex(columns=model_columns, fill_value=0)

    # Predict
    prediction = model.predict(df)[0]
    return {"prediction": int(prediction)}
