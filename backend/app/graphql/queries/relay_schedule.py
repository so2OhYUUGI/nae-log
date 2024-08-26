import strawberry
from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.schedule import Schedule as ScheduleSchema
from app.db.crud.crud_schedule import schedule as crud_schedule

@strawberry.type
class ScheduleType:
    id: int
    relay_id: int
    job_id: str
    name: str
    cron: str
    active: bool
    next_run_time: Optional[str]

@strawberry.type
class ScheduleQuery:
    @strawberry.field
    def relay_schedules(self, relay_id: Optional[int] = None) -> List[ScheduleType]:
        db: Session = SessionLocal()
        if relay_id is not None:
            schedules = crud_schedule.get_by_relay_id(db, relay_id=relay_id)
        else:
            schedules = db.query(ScheduleSchema).all()
        return [ScheduleType(**schedule.__dict__) for schedule in schedules]

# Mutationは必要に応じて追加
