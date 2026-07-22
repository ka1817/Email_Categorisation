from fastapi import FastAPI
from src.model_prediction import ModelPrediction

from database import engine, SessionLocal
from models import Base, PredictionLog

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Email Categorization API",
    version="1.0.0"
)

# Load ML model once
predictor = ModelPrediction()


@app.get("/")
def home():
    return {
        "message": "Welcome to Email Categorization API"
    }


@app.get("/predict")
def predict(email: str):

    # Predict category
    prediction = predictor.predict(email)

    # Create database session
    db = SessionLocal()

    try:
        # Save prediction to PostgreSQL
        log = PredictionLog(
            email=email,
            prediction=prediction
        )

        db.add(log)
        db.commit()
        db.refresh(log)

    finally:
        db.close()

    return {
        "email": email,
        "prediction": prediction
    }