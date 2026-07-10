"""
src/model_prediction.py

Load the trained model and make predictions.
"""

import os
import logging
import joblib


logger = logging.getLogger(__name__)


class ModelPrediction:
    """
    Predict email categories using a trained Pipeline.
    """

    def __init__(
        self,
        model_path: str = "artifacts/email_classifier.pkl",
    ):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        """
        Load the trained pipeline.
        """

        logger.info("Loading model...")

        if not os.path.exists(self.model_path):
            raise FileNotFoundError(
                f"Model not found: {self.model_path}"
            )

        model = joblib.load(self.model_path)

        logger.info("Model loaded successfully.")

        return model

    def predict(self, text: str) -> str:
        

        prediction = self.model.predict([text])

        return prediction[0]

    def predict_proba(self, text: str):
      

        probabilities = self.model.predict_proba([text])[0]

        classes = self.model.classes_

        return {
            label: round(prob, 4)
            for label, prob in zip(classes, probabilities)
        }