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
    relay_id = Column(Integer, index=True)  # リレーID（Relayテーブルとの関連）
    job_id = Column(String, index=True, unique=True)  # ジョブの一意識別子
    name = Column(String, index=True)  # スケジュールの名前
    cron = Column(String)  # Cron形式のスケジュール
    active = Column(Boolean, default=True)  # スケジュールの有効/無効
    next_run_time = Column(DateTime)  # 次回実行時間
    action = Column(String)  # リレーのon/off指定を追加

# Pydantic Base Model
class AutomationScheduleBase(BaseModel):
    relay_id: int
    job_id: str
    name: str
    cron: str
    active: Optional[bool] = True
    next_run_time: Optional[datetime] = None
    action: Optional[str]  # "on"または"off"を指定

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
    action: Optional[str]

@strawberry.input
class AutomationScheduleInput:
    field_id: int
    relay_id: int
    time: str  # "HH:MM" format
    action: str  # "on" or "off"
    active: Optional[bool] = True