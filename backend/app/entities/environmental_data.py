# app/entities/environmental_data.py
from typing import Optional
from sqlalchemy import Column, Integer, Float, Boolean, DateTime
import strawberry
from pydantic import BaseModel
from datetime import datetime

from app.db.base_class import Base

# EnvironmentalData Model (SQLAlchemy ORM Model)
class EnvironmentalData(Base):
    __tablename__ = "environmental_data"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    temperature = Column(Float)
    humidity = Column(Float)
    relay_status = Column(Boolean)
    field_id = Column(Integer, index=True)

# Pydantic Base Model
class EnvironmentalDataBase(BaseModel):
    timestamp: datetime
    temperature: Optional[float]
    humidity: Optional[float]
    relay_status: Optional[bool]
    field_id: int

    class Config:
        from_attributes = True

class EnvironmentalDataCreate(EnvironmentalDataBase):
    pass

class EnvironmentalDataUpdate(EnvironmentalDataBase):
    pass

# Pydantic DB Schema
class EnvironmentalDataInDBBase(EnvironmentalDataBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class EnvironmentalDataSchema:
    id: int
    timestamp: datetime
    temperature: Optional[float]
    humidity: Optional[float]
    relay_status: Optional[bool]
    field_id: int
