from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataPreprocessing
from src.model_training import ModelTrainer
from src.training_rnn import TrainingRNN
from config import DATA_PATH
import warnings
warnings.filterwarnings('ignore')
import sklearn

print("Sklearn version:", sklearn.__version__)
# Load data
preprocessor=TrainingRNN(10,32)
df = DataIngestion(DATA_PATH).load_data()
X_train_pad,y_train,X_test_pad,y_test,tokenizer =preprocessor.preprocess(df)
model=preprocessor.train(X_train_pad,y_train)
preprocessor.evaluate(X_test_pad,y_test)
