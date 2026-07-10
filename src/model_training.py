"""
src/model_training.py

Train and save the email classification model.
"""

import os
import logging
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


logger = logging.getLogger(__name__)


class ModelTrainer:
    """
    Train and save a TF-IDF + Logistic Regression model.
    """

    def __init__(
        self,
        test_size=0.2,
        random_state=42
    ):
        self.test_size = test_size
        self.random_state = random_state

        self.pipeline = Pipeline([
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    stop_words="english",
                    max_features=10000,
                    ngram_range=(1, 2),
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    max_iter=1000,
                    random_state=self.random_state,
                ),
            ),
        ])

    def train(self, df):

        logger.info("Preparing train and test datasets...")

        X = df["text"]
        y = df["category"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=self.test_size,
            random_state=self.random_state,
            stratify=y,
        )

        logger.info("Training model...")

        self.pipeline.fit(X_train, y_train)

        logger.info("Making predictions...")

        y_pred = self.pipeline.predict(X_test)

        accuracy = accuracy_score(y_test, y_pred)

        logger.info("Training completed.")
        logger.info("Accuracy: %.4f", accuracy)

        return {
            "accuracy": accuracy,
            "classification_report": classification_report(
                y_test,
                y_pred,
            ),
            "confusion_matrix": confusion_matrix(
                y_test,
                y_pred,
            ),
        }

    def save_model(
        self,
        model_path="artifacts/email_classifier.pkl",
    ):
        """
        Save the trained pipeline.
        """

        os.makedirs(
            os.path.dirname(model_path),
            exist_ok=True,
        )

        joblib.dump(self.pipeline, model_path)

        logger.info("Model saved to %s", model_path)