# app/entities/notification_schedule.py
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, DateTime
import strawberry
from pydantic import BaseModel
from datetime import datetime

from app.db.base_class import Base

# NotificationSchedule Model (SQLAlchemy ORM Model)
class NotificationSchedule(Base):
    __tablename__ = "notification_schedules"

    id = Column(Integer, primary_key=True, index=True)
    plant_id = Column(Integer, index=True)
    task_type = Column(String, index=True)
    description = Column(String)
    cron = Column(String)
    active = Column(Boolean, default=True)
    next_run_time = Column(DateTime)

# Pydantic Base Model
class NotificationScheduleBase(BaseModel):
    plant_id: int
    task_type: str
    description: str
    cron: str
    active: Optional[bool] = True
    next_run_time: Optional[datetime] = None

    class Config:
        from_attributes = True

class NotificationScheduleCreate(NotificationScheduleBase):
    pass

class NotificationScheduleUpdate(NotificationScheduleBase):
    pass

# Pydantic DB Schema
class NotificationScheduleInDBBase(NotificationScheduleBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class NotificationScheduleSchema:
    id: int
    plant_id: int
    task_type: str
    description: str
    cron: str
    active: bool
    next_run_time: Optional[datetime]
