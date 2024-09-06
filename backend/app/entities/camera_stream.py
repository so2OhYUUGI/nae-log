# app/entities/camera_stream.py
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean
import strawberry
from pydantic import BaseModel

from app.db.base_class import Base

# CameraStream Model (SQLAlchemy ORM Model)
class CameraStream(Base):
    __tablename__ = "camera_streams"

    id = Column(Integer, primary_key=True, index=True)
    stream_url = Column(String, index=True)
    description = Column(String)
    active = Column(Boolean, default=True)
    field_id = Column(Integer, index=True)

# Pydantic Base Model
class CameraStreamBase(BaseModel):
    stream_url: str
    description: str
    active: Optional[bool] = True
    field_id: int

    class Config:
        from_attributes = True

class CameraStreamCreate(CameraStreamBase):
    pass

class CameraStreamUpdate(CameraStreamBase):
    pass

# Pydantic DB Schema
class CameraStreamInDBBase(CameraStreamBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class CameraStreamSchema:
    id: int
    stream_url: str
    description: str
    active: bool
    field_id: int
