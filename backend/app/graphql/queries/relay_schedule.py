# app/graphql/queries/relay_schedule.py
import strawberry
from typing import List, Optional
from app.db.session import SessionLocal
from app.entities.schedule import Schedule as ScheduleModel, ScheduleSchema
from sqlalchemy.orm import Session

@strawberry.type
class ScheduleQuery:
    @strawberry.field
    def relay_schedule(self, id: int) -> Optional[ScheduleSchema]:
        db: Session = SessionLocal()
        schedule = db.query(ScheduleModel).filter(ScheduleModel.id == id).first()
        return schedule

    @strawberry.field
    def relay_all_schedules(self) -> List[ScheduleSchema]:
        db: Session = SessionLocal()
        schedules = db.query(ScheduleModel).all()
        return schedules
