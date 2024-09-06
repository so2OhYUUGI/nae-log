import strawberry
from typing import List, Optional
from app.db.session import SessionLocal
from app.entities.automation_schedule import AutomationSchedule, AutomationScheduleSchema
from app.entities.relay import Relay
from sqlalchemy.orm import Session
from sqlalchemy import and_

@strawberry.type
class ScheduleQuery:

    @strawberry.field
    def relay_schedule(
        self,
        id: Optional[int] = None,
        job_id: Optional[str] = None,
        relay_id: Optional[int] = None,
        field_id: Optional[int] = None
    ) -> List[AutomationScheduleSchema]:
        """
        スケジュールを取得するクエリ。
        提供された引数に基づいてフィルタリングを行います。
        """
        with SessionLocal() as db:
            query = db.query(AutomationSchedule)

            # フィルタ条件を格納するリスト
            filters = []

            if id is not None:
                filters.append(AutomationSchedule.id == id)

            if job_id is not None:
                filters.append(AutomationSchedule.job_id == job_id)

            if relay_id is not None:
                filters.append(AutomationSchedule.relay_id == relay_id)

            if field_id is not None:
                # フィールドIDに関連するリレーIDを取得
                relays = db.query(Relay).filter(Relay.field_id == field_id).all()
                relay_ids = [relay.id for relay in relays]
                if relay_ids:
                    filters.append(AutomationSchedule.relay_id.in_(relay_ids))
                else:
                    # 指定されたフィールドIDに関連するリレーがない場合、空のリストを返す
                    return []

            # フィルタを適用
            if filters:
                schedules = query.filter(and_(*filters)).all()
            else:
                # フィルタがない場合は全てのスケジュールを取得
                schedules = query.all()

            # スケジュールをシリアライズして返す
            return [
                AutomationScheduleSchema(
                    id=schedule.id,
                    relay_id=schedule.relay_id,
                    job_id=schedule.job_id,
                    name=schedule.name,
                    cron=schedule.cron,
                    active=schedule.active,
                    next_run_time=schedule.next_run_time,
                    action=schedule.action
                ) for schedule in schedules
            ]
