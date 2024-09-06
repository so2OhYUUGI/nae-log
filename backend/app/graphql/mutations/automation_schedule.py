# app/graphql/mutations/automation_schedule.py
import strawberry
from typing import Optional
from app.db.session import SessionLocal
from app.entities.automation_schedule import AutomationSchedule, AutomationScheduleSchema, AutomationScheduleInput
from app.entities.relay import Relay
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.core.scheduler import scheduler
from app.utils.relay_utils import get_relay_action  # 追加: get_relay_actionのインポート

@strawberry.type
class RelayScheduleMutation:
    @strawberry.mutation
    def create_relay_schedule(
        self,
        input: AutomationScheduleInput
    ) -> AutomationScheduleSchema:
        """
        新しいリレースケジュールを作成するミューテーション。
        """
        with SessionLocal() as db:
            # リレーが指定されたフィールドに存在するか確認
            relay = db.query(Relay).filter(Relay.id == input.relay_id, Relay.field_id == input.field_id).first()
            if not relay:
                raise ValueError(f"Relay with ID {input.relay_id} not found in Field with ID {input.field_id}")

            # スケジュールのcron形式を生成 (毎日の指定時刻)
            cron_time = RelayScheduleMutation._generate_cron_time(input.time)

            # スケジュールを作成
            schedule = AutomationSchedule(
                relay_id=input.relay_id,
                job_id=f"{input.relay_id}_{input.time}_{input.action}",
                name=f"Relay {input.relay_id} {input.action} at {input.time}",
                cron=cron_time,
                active=input.active,
                action=input.action,
                next_run_time=RelayScheduleMutation._calculate_next_run_time(input.time)
            )

            db.add(schedule)
            db.commit()
            db.refresh(schedule)

            # スケジュール登録 (on/off アクションに基づいて)
            RelayScheduleMutation._schedule_relay_job(
                schedule.job_id, input.action, input.time, input.relay_id
            )

            return AutomationScheduleSchema(
                id=schedule.id,
                relay_id=schedule.relay_id,
                job_id=schedule.job_id,
                name=schedule.name,
                cron=schedule.cron,
                active=schedule.active,
                next_run_time=schedule.next_run_time,
                action=schedule.action
            )

    @strawberry.mutation
    def update_relay_schedule(
        self,
        id: int,
        input: AutomationScheduleInput
    ) -> AutomationScheduleSchema:
        """
        既存のリレースケジュールを更新するミューテーション。
        """
        with SessionLocal() as db:
            # 更新対象のスケジュールを取得
            schedule = db.query(AutomationSchedule).filter(AutomationSchedule.id == id).first()
            if not schedule:
                raise ValueError(f"Schedule with ID {id} not found.")

            # フィールドIDとリレーIDの関連チェック
            if input.relay_id is not None:
                relay = db.query(Relay).filter(Relay.id == input.relay_id, Relay.field_id == input.field_id).first()
                if not relay:
                    raise ValueError(f"Relay with ID {input.relay_id} not found in Field with ID {input.field_id}")
                schedule.relay_id = input.relay_id

            # timeが指定されている場合、cronとnext_run_timeを更新
            if input.time:
                schedule.cron = RelayScheduleMutation._generate_cron_time(input.time)
                schedule.next_run_time = RelayScheduleMutation._calculate_next_run_time(input.time)

            # その他のフィールドの更新
            if input.action:
                schedule.action = input.action
            if input.active is not None:
                schedule.active = input.active

            db.commit()
            db.refresh(schedule)

            # スケジュール更新 (on/off アクションに基づいて)
            RelayScheduleMutation._schedule_relay_job(
                schedule.job_id, input.action, input.time, input.relay_id
            )

            return AutomationScheduleSchema(
                id=schedule.id,
                relay_id=schedule.relay_id,
                job_id=schedule.job_id,
                name=schedule.name,
                cron=schedule.cron,
                active=schedule.active,
                next_run_time=schedule.next_run_time,
                action=schedule.action
            )

    @staticmethod
    def _generate_cron_time(time: str) -> str:
        """
        "HH:MM" の形式で受け取った時間から、cron形式のスケジュールを生成。
        """
        hour, minute = time.split(":")
        return f"{minute} {hour} * * *"

    @staticmethod
    def _calculate_next_run_time(time: str) -> datetime:
        """
        次回実行予定時間を計算する関数。現在時刻を基にして、次の指定時刻を計算する。
        """
        now = datetime.now()
        hour, minute = map(int, time.split(":"))
        next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        # もし次の実行時間が現在時刻より前なら、翌日に設定
        if next_run < now:
            next_run += timedelta(days=1)
        return next_run

    @staticmethod
    def _schedule_relay_job(job_id: str, action: str, time: str, relay_id: int):
        """
        リレーのon/offをcronスケジュールに追加または更新する。
        リレーIDを指定して対応するリレーを操作する。
        """
        hour, minute = map(int, time.split(":"))
        job_function = get_relay_action(action)  # 変更: relay_utilsからインポートした関数を使用

        # 既存のジョブがあれば更新、なければ新規作成
        if scheduler.get_job(job_id):
            scheduler.reschedule_job(job_id, trigger='cron', hour=hour, minute=minute)
            print(f"Scheduler updated for action {action} at {hour:02}:{minute:02} for relay {relay_id}.")
        else:
            scheduler.add_job(job_function, 'cron', hour=hour, minute=minute, id=job_id, args=[relay_id])
            print(f"Scheduler added for action {action} at {hour:02}:{minute:02} for relay {relay_id}.")
