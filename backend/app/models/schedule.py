# app/models/schedule.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.db.base_class import Base

class Schedule(Base):
    __tablename__ = "schedules"  # テーブル名を指定

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    cron = Column(String)  # cron式
    active = Column(Boolean, default=True)
    next_run_time = Column(DateTime)
