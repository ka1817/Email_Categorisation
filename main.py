"""
main.py

Entry point for Email Classification project.
"""

import logging

from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataPreprocessing
from src.model_training import ModelTrainer
from config import DATA_PATH
from src.training_rnn import TrainingRNN

import pandas as pd
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
df=pd.read_csv(DATA_PATH)
processor=TrainingRNN(10,32)
X_train_pad,y_train,X_test_pad,y_test,tokenizer=processor.preprocess(df)
model=processor.train(X_train_pad,y_train)
print(model.evaluate(X_test_pad,y_test))
print("Results1")


