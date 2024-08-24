from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.core.gpio import power_supply_relay
from app.core.scheduler import scheduler

from .constants import JOB_ID

router = APIRouter()

class RelaySchedule(BaseModel):
    action: Literal['on', 'off']
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)

def on_relay():
    power_supply_relay[0].on()

def off_relay():
    power_supply_relay[0].off()

def schedule_relay_job(job_id: str, action: str, hour: int, minute: int):
    job_function = on_relay if action == "on" else off_relay
    if scheduler.get_job(job_id):
        # 既存のジョブがあれば更新
        scheduler.reschedule_job(job_id, trigger='cron', hour=hour, minute=minute)
        print(f"Scheduler updated for action {action} with new time {hour:02}:{minute:02}.")
    else:
        # ジョブが存在しない場合は新規作成
        scheduler.add_job(job_function, 'cron', hour=hour, minute=minute, id=job_id)
        print(f"Scheduler started and job added for action {action}.")

@router.post("/")
def schedule_relay_action(schedule: RelaySchedule) -> dict:
    # 受け取ったデータを出力
    print(f"Received action: {schedule.action}, time: {schedule.hour:02}:{schedule.minute:02}")

    if schedule.action in ["on", "off"]:
        __job_id = f'{schedule.action}_{JOB_ID}'
        schedule_relay_job(__job_id, schedule.action, schedule.hour, schedule.minute)
    else:
        raise HTTPException(status_code=400, detail="Invalid action. Must be 'on' or 'off'.")

    return {"message": f"Relay scheduled to turn {schedule.action} at {schedule.hour:02}:{schedule.minute:02}."}
