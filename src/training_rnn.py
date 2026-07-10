import tensorflow as tf
import os
import pickle

from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from sklearn.metrics import classification_report
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from sklearn.model_selection import train_test_split
import numpy as np
class TrainingRNN:
    def __init__(self,epochs,batch_size):
        self.epochs=epochs
        self.batch_size=batch_size 
        self.VOCAB_SIZE =10000
        self.MAX_LEN=100
        self.model=None
        self.tokenizer=None
        self.label_encoder=None
    def preprocess(self,df):
        X = df["text"].values
        y = df["category"].values

# Encode labels
        self.label_encoder = LabelEncoder()
        y = self.label_encoder.fit_transform(y)

# Train-test split
        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)
        self.VOCAB_SIZE = 10000
        self.MAX_LEN = 100

        self.tokenizer = Tokenizer(num_words=self.VOCAB_SIZE, oov_token="<OOV>")

        self.tokenizer.fit_on_texts(X_train)

        train_sequences = self.tokenizer.texts_to_sequences(X_train)
        test_sequences = self.tokenizer.texts_to_sequences(X_test)

        X_train_pad = pad_sequences(train_sequences,maxlen=self.MAX_LEN,padding="post",truncating="post")

        X_test_pad = pad_sequences(test_sequences,maxlen=self.MAX_LEN,padding="post", truncating="post")

        return X_train_pad,y_train,X_test_pad,y_test,self.tokenizer
    def train(self,X_train_pad,y_train):
        self.model = Sequential([
        Embedding(
        input_dim=self.VOCAB_SIZE,
        output_dim=128,
        input_length=self.MAX_LEN
                        ),

        SimpleRNN(64),

        Dense(32, activation="relu"),

        Dense(6, activation="softmax")
])
        self.model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

        history = self.model.fit(
          X_train_pad,
          y_train,
          epochs=self.epochs,
          batch_size=self.batch_size,
          validation_split=0.2
)
        return self.model 
    def evaluate(self,X_test_pad,y_test):
        y_pred = self.model.predict(X_test_pad)

        y_pred = np.argmax(y_pred, axis=1)

        print(classification_report(
            y_test,
            y_pred,
            target_names=self.label_encoder.classes_))

    def save_artifacts(self):

    # Create artifacts directory if it doesn't exist
        os.makedirs("artifacts", exist_ok=True)

    # File paths
        model_path = os.path.join("artifacts", "email_classifier.keras")
        tokenizer_path = os.path.join("artifacts", "tokenizer.pkl")
        label_encoder_path = os.path.join("artifacts", "label_encoder.pkl")

    # Validate objects
        if self.model is None:
           raise ValueError("Model has not been trained.")

        if self.tokenizer is None:
           raise ValueError("Tokenizer has not been initialized.")

        if self.label_encoder is None:
           raise ValueError("LabelEncoder has not been initialized.")

    # Save Keras model
        self.model.save(model_path)

    # Save tokenizer
        with open(tokenizer_path, "wb") as f:
            pickle.dump(self.tokenizer, f)

    # Save label encoder
        with open(label_encoder_path, "wb") as f:
            pickle.dump(self.label_encoder, f)

        print("Artifacts saved successfully!")
        print(f"Model         : {model_path}")
        print(f"Tokenizer     : {tokenizer_path}")
        print(f"Label Encoder : {label_encoder_path}")