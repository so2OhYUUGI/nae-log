# app/entities/plant.py
from typing import Optional
from sqlalchemy import Column, Integer, String, Date, DateTime
import strawberry
from pydantic import BaseModel
from datetime import datetime

from app.db.base_class import Base

# Plant Model (SQLAlchemy ORM Model)
class Plant(Base):
    __tablename__ = "plants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    species = Column(String)
    planting_date = Column(Date)
    end_date = Column(Date)
    status = Column(String, index=True)
    last_updated = Column(DateTime, default=datetime.utcnow)
    field_id = Column(Integer, index=True)

# Pydantic Base Model
class PlantBase(BaseModel):
    name: str
    species: str
    planting_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: str
    last_updated: Optional[datetime] = None
    field_id: int

    class Config:
        from_attributes = True

class PlantCreate(PlantBase):
    pass

class PlantUpdate(PlantBase):
    pass

# Pydantic DB Schema
class PlantInDBBase(PlantBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class PlantSchema:
    id: int
    name: str
    species: str
    planting_date: Optional[datetime]
    end_date: Optional[datetime]
    status: str
    last_updated: Optional[datetime]
    field_id: int
