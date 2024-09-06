from sqlalchemy import Column, Integer, String, DateTime
import strawberry
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from app.db.base_class import Base

# Field Model (SQLAlchemy ORM Model)
class Field(Base):
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Pydantic Base Model
class FieldBase(BaseModel):
    name: str
    location: str

    class Config:
        from_attributes = True

class FieldCreate(FieldBase):
    pass

class FieldUpdate(FieldBase):
    pass

# Pydantic DB Schema
class FieldInDBBase(FieldBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class FieldType:
    id: int
    name: str
    location: Optional[str]
    created_at: datetime

@strawberry.input
class FieldInput:
    name: str
    location: Optional[str]
