# app/entities/schedule.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.base_class import Base
import strawberry
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schedule Model (SQLAlchemy ORM Model)
class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    relay_id = Column(Integer, index=True)
    job_id = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    cron = Column(String)
    active = Column(Boolean, default=True)
    next_run_time = Column(DateTime)

# Pydantic Base Model
class ScheduleBase(BaseModel):
    relay_id: int
    job_id: str
    name: str
    cron: str
    active: Optional[bool] = True
    next_run_time: Optional[datetime] = None

    class Config:
        from_attributes = True

# Pydantic Create and Update Schemas
class ScheduleCreate(ScheduleBase):
    pass

class ScheduleUpdate(ScheduleBase):
    pass

# Pydantic DB Schema
class ScheduleInDBBase(ScheduleBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class ScheduleSchema:
    id: int
    relay_id: int
    job_id: str
    name: str
    cron: str
    active: bool
    next_run_time: Optional[datetime]
