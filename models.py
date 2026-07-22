from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base = declarative_base()


class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False)
    prediction = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)