# app/entities/observation.py
from sqlalchemy import Column, Integer, String, DateTime
import strawberry
from pydantic import BaseModel
from datetime import datetime

from app.db.base_class import Base

# Observation Model (SQLAlchemy ORM Model)
class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, index=True)
    observation_date = Column(DateTime, default=datetime.utcnow)
    comment = Column(String)
    observer_name = Column(String)

# Pydantic Base Model
class ObservationBase(BaseModel):
    plant_id: int
    observation_date: datetime
    comment: str
    observer_name: str

    class Config:
        from_attributes = True

class ObservationCreate(ObservationBase):
    pass

class ObservationUpdate(ObservationBase):
    pass

# Pydantic DB Schema
class ObservationInDBBase(ObservationBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class ObservationSchema:
    id: int
    plant_id: int
    observation_date: datetime
    comment: str
    observer_name: str
