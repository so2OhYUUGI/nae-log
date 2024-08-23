from fastapi import APIRouter
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# relayTimer.py からインポートする場合は、scheduler と job_id を共有します
from .main import job_id, scheduler

router = APIRouter()

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
