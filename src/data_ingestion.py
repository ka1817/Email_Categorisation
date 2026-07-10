"""
src/data_ingestion.py
"""

import os
import logging
import pandas as pd


logger = logging.getLogger(__name__)


class DataIngestion:
    REQUIRED_COLUMNS = ["text", "category"]

    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:

        logger.info("Loading dataset...")

        if not os.path.exists(self.data_path):
            raise FileNotFoundError(
                f"Dataset not found: {self.data_path}"
            )

        try:
            df = pd.read_csv(self.data_path)

            self.validate_data(df)

            logger.info(f"Dataset loaded successfully. Shape: {df.shape}")

            return df

        except Exception as e:
            logger.exception("Error while loading dataset.")
            raise e

    def validate_data(self, df: pd.DataFrame):
        """
        Validate dataset.
        """

        if df.empty:
            raise ValueError("Dataset is empty.")

        missing_columns = [
            col for col in self.REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}"
            )

        duplicates = df.duplicated().sum()

        if duplicates > 0:
            logger.warning(f"Removing {duplicates} duplicate rows.")
            df.drop_duplicates(inplace=True)

        nulls = df.isnull().sum().sum()

        if nulls > 0:
            logger.warning(f"Removing rows with missing values ({nulls}).")
            df.dropna(inplace=True)

        logger.info("Dataset validation completed successfully.")
