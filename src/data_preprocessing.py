"""
src/data_preprocessing.py

Text preprocessing module for Email Classification.
"""

import re
import logging
import pandas as pd


logger = logging.getLogger(__name__)


class DataPreprocessing:
    """
    Handles preprocessing of email text.
    """

    REQUIRED_COLUMN = "text"

    def __init__(self):
        pass

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        
        logger.info("Starting text preprocessing...")

        df = df.copy()

        if self.REQUIRED_COLUMN not in df.columns:
            raise ValueError(
                f"'{self.REQUIRED_COLUMN}' column not found in dataframe."
            )

        df[self.REQUIRED_COLUMN] = (
            df[self.REQUIRED_COLUMN]
            .fillna("")
            .astype(str)
            .apply(self.clean_text)
        )

        logger.info("Text preprocessing completed successfully.")

        return df

    @staticmethod
    def clean_text(text: str) -> str:
        

        text = text.lower()

        text = re.sub(r"<.*?>", " ", text)

        text = re.sub(r"http\S+|www\S+", " ", text)

        text = re.sub(r"\s+", " ", text).strip()

        return text