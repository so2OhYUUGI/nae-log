from sqlalchemy.orm import Session
from typing import List, Optional
from app.db.models.schedule import Schedule
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate

class CRUDSchedule:
    def get_by_relay_id(self, db: Session, relay_id: int) -> List[Schedule]:
        return db.query(Schedule).filter(Schedule.relay_id == relay_id).all()

    def create_with_relay_id(self, db: Session, obj_in: ScheduleCreate, relay_id: int) -> Schedule:
        db_obj = Schedule(**obj_in.dict(), relay_id=relay_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, db_obj: Schedule, obj_in: ScheduleUpdate) -> Schedule:
        for field, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, id: int) -> Schedule:
        obj = db.query(Schedule).get(id)
        db.delete(obj)
        db.commit()
        return obj

schedule = CRUDSchedule()
