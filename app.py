from fastapi import FastAPI
from src.model_prediction import ModelPrediction

app = FastAPI(
    title="Email Categorization API",
    version="1.0.0"
)

# Load model once
predictor = ModelPrediction()


@app.get("/")
def home():
    return {"message": "Welcome to Email Categorization API"}


@app.get("/predict")
def predict(email: str):
    prediction = predictor.predict(email)

    return {
        "email": email,
        "prediction": prediction
    }