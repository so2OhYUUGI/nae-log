from sqlalchemy import Column, Integer, String
import strawberry
from pydantic import BaseModel

from app.db.base_class import Base

# Sensor Model (SQLAlchemy ORM Model)
class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    sensor_type = Column(String, index=True)
    description = Column(String)
    field_id = Column(Integer, index=True)

# Pydantic Base Model
class SensorBase(BaseModel):
    sensor_type: str
    description: str
    field_id: int

    class Config:
        from_attributes = True

class SensorCreate(SensorBase):
    pass

class SensorUpdate(SensorBase):
    pass

# Pydantic DB Schema
class SensorInDBBase(SensorBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class SensorSchema:
    id: int
    sensor_type: str
    description: str
    field_id: int
