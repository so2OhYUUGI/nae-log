from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.entities.automation_schedule import AutomationScheduleBase as ScheduleModel, AutomationScheduleCreate, AutomationScheduleUpdate
from app.crud.schedule import get_schedules_by_relay, create_schedule, update_schedule
from app.db.session import SessionLocal

router = APIRouter()

# データベースセッションを取得する依存関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/schedules/{relay_id}", response_model=List[ScheduleModel])
def read_schedules_by_relay(relay_id: int, db: Session = Depends(get_db)):
    schedules = get_schedules_by_relay(db, relay_id=relay_id)
    return schedules

@router.post("/schedules/", response_model=ScheduleModel)
def create_new_schedule(schedule: AutomationScheduleCreate, db: Session = Depends(get_db)):
    return create_schedule(db=db, schedule=schedule)

@router.put("/schedules/{id}", response_model=ScheduleModel)
def update_existing_schedule(id: int, schedule: AutomationScheduleUpdate, db: Session = Depends(get_db)):
    return update_schedule(db=db, schedule=schedule, schedule_id=id)
