# app/graphql/queries/relay_schedule.py
import strawberry
from typing import List, Optional
from app.db.session import SessionLocal
from app.entities.automation_schedule import AutomationScheduleBase, AutomationScheduleSchema  # 修正
from sqlalchemy.orm import Session

@strawberry.type
class ScheduleQuery:
    @strawberry.field
    def relay_schedule(self, id: int) -> Optional[AutomationScheduleSchema]:
        db: Session = SessionLocal()
        schedule = db.query(AutomationScheduleBase).filter(AutomationScheduleBase.id == id).first()
        return schedule

    @strawberry.field
    def relay_all_schedules(self) -> List[AutomationScheduleSchema]:
        db: Session = SessionLocal()
        schedules = db.query(AutomationScheduleBase).all()
        return schedules
