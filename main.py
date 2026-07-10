"""
main.py

Entry point for Email Classification project.
"""

import logging

from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataPreprocessing
from src.model_training import ModelTrainer
from config import DATA_PATH


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)


def main():

    try:
        # Load dataset
        ingestion = DataIngestion(DATA_PATH)
        df = ingestion.load_data()

        # Preprocess text
        preprocessing = DataPreprocessing()
        df = preprocessing.preprocess(df)

        # Train model
        trainer = ModelTrainer()
        results = trainer.train(df)

        # Print evaluation metrics
        print("\n========== Model Performance ==========")
        print(f"Accuracy: {results['accuracy']:.4f}\n")

        print("Classification Report:")
        print(results["classification_report"])

        print("Confusion Matrix:")
        print(results["confusion_matrix"])

        # Save model
        trainer.save_model()

        print("\nModel saved successfully in artifacts/email_classifier.pkl")

    except Exception as e:
        logging.exception("Application failed.")
        raise e


if __name__ == "__main__":
    main()
