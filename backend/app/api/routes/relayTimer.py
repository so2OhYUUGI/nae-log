from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.gpio import relay

router = APIRouter()

# Pydanticモデルを作成
class RelaySchedule(BaseModel):
    action: str  # onまたはoff
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)

def tick():
    relay.on()
    print("Tick! The scheduled task is running.")

# スケジューラのインスタンスを作成
scheduler = BackgroundScheduler()
scheduler.start()
job_id = "relay_job"

@router.get("/")
def get_relay_schedule():
    job = scheduler.get_job(job_id)
    if job:
        trigger = job.trigger
        action = "on" if job.next_run_time else "off"
        # hourとminuteの値を取得
        hour_index = CronTrigger.FIELD_NAMES.index('hour')
        hour = trigger.fields[hour_index].expressions[0].first
        minute_index = CronTrigger.FIELD_NAMES.index('minute')
        minute = trigger.fields[minute_index].expressions[0].first
        return {"action": action, "hour": hour, "minute": minute}
    else:
        return {"message": "No active schedule found."}

@router.post("/")
def schedule_relay_action(schedule: RelaySchedule):
    # 受け取ったデータを出力
    print(f"Received action: {schedule.action}, time: {schedule.hour:02}:{schedule.minute:02}")
    
    if schedule.action == "on":
        if scheduler.get_job(job_id):
            # 既存のジョブがあれば更新
            scheduler.reschedule_job(job_id, trigger='cron', hour=schedule.hour, minute=schedule.minute)
            print("Scheduler updated with new time.")
        else:
            # ジョブが存在しない場合は新規作成
            scheduler.add_job(tick, 'cron', hour=schedule.hour, minute=schedule.minute, id=job_id)
            print("Scheduler started and job added.")
    elif schedule.action == "off":
        if scheduler.get_job(job_id):
            # 特定のジョブのみを削除
            scheduler.remove_job(job_id)
            print("Scheduler job stopped.")
        else:
            print("No active job found to stop.")
    else:
        raise HTTPException(status_code=400, detail="Invalid action. Must be 'on' or 'off'.")

    return {"message": f"Relay scheduled to turn {schedule.action} at {schedule.hour:02}:{schedule.minute:02}."}
