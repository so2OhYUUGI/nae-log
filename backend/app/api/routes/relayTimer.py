from fastapi import APIRouter
from pydantic import BaseModel, Field
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

router = APIRouter()

# スケジューラのインスタンスをグローバルに宣言
scheduler = BackgroundScheduler()
scheduler.start()

class RelaySchedule(BaseModel):
    action: str
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)

def tick():
    print('This is a test tick')

@router.post("/")
def schedule_relay_action(schedule: RelaySchedule):
    # actionが'on'の場合はジョブを追加
    if schedule.action == "on":
        print(f"Scheduling relay to turn on at {schedule.hour:02}:{schedule.minute:02}")
        
        # 同じジョブが存在する場合は追加しない
        if not scheduler.get_job('relay_on_job'):
            trigger = CronTrigger(hour=schedule.hour, minute=schedule.minute)
            scheduler.add_job(tick, trigger, id='relay_on_job')
        else:
            return {"message": "Relay on job is already scheduled."}

    # actionが'off'の場合はジョブを削除
    elif schedule.action == "off":
        print("Stopping the relay schedule")
        scheduler.remove_job('relay_on_job')
        
    return {"message": f"Relay action {schedule.action} scheduled at {schedule.hour:02}:{schedule.minute:02}."}

@router.get("/")
def get_relay_schedule():
    job = scheduler.get_job('relay_on_job')
    if job:
        trigger = job.trigger
        hour_index = CronTrigger.FIELD_NAMES.index('hour')
        minute_index = CronTrigger.FIELD_NAMES.index('minute')
        hour = trigger.fields[hour_index].expressions[0].first
        minute = trigger.fields[minute_index].expressions[0].first
        return {"action": "on", "hour": hour, "minute": minute}
    else:
        return {"action": "off", "hour": None, "minute": None}
