# app/crud/schedule.py
from sqlalchemy.orm import Session
from app.entities.automation_schedule import AutomationScheduleSchema, AutomationScheduleCreate, AutomationScheduleUpdate  # 修正

def get_schedules_by_relay(db: Session, relay_id: int):
    return db.query(AutomationScheduleSchema).filter(AutomationScheduleSchema.relay_id == relay_id).all()

def create_schedule(db: Session, schedule: AutomationScheduleCreate):
    db_schedule = AutomationScheduleSchema(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

def update_schedule(db: Session, schedule: AutomationScheduleUpdate, schedule_id: int):
    db_schedule = db.query(AutomationScheduleSchema).filter(AutomationScheduleSchema.id == schedule_id).first()
    if not db_schedule:
        return None
    for key, value in schedule.dict().items():
        setattr(db_schedule, key, value)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule

