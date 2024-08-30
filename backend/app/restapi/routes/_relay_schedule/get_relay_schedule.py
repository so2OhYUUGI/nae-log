from fastapi import APIRouter
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from app.core.scheduler import scheduler
from .constants import JOB_ID

router = APIRouter()

@router.get("/")
def get_relay_schedule():
    job = scheduler.get_job(JOB_ID)
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

@router.get("/{relay_id}")
def get_relay_status(relay_id: int):
    # relay_id が整数であることを期待しています
    return {"relay_id": relay_id}