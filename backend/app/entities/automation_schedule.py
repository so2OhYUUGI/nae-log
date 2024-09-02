# app/entities/automation_schedule.py
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, DateTime
import strawberry
from pydantic import BaseModel
from datetime import datetime

from app.db.base_class import Base

# AutomationSchedule Model (SQLAlchemy ORM Model)
class AutomationSchedule(Base):
    __tablename__ = "automation_schedules"

    id = Column(Integer, primary_key=True, index=True)
    relay_id = Column(Integer, index=True)
    job_id = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    cron = Column(String)
    active = Column(Boolean, default=True)
    next_run_time = Column(DateTime)

# Pydantic Base Model
class AutomationScheduleBase(BaseModel):
    relay_id: int
    job_id: str
    name: str
    cron: str
    active: Optional[bool] = True
    next_run_time: Optional[datetime] = None

    class Config:
        from_attributes = True

class AutomationScheduleCreate(AutomationScheduleBase):
    pass

class AutomationScheduleUpdate(AutomationScheduleBase):
    pass

# Pydantic DB Schema
class AutomationScheduleInDBBase(AutomationScheduleBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class AutomationScheduleSchema:
    id: int
    relay_id: int
    job_id: str
    name: str
    cron: str
    active: bool
    next_run_time: Optional[datetime]
