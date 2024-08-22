from config import PUBLIC_PATH

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from apscheduler.schedulers.background import BackgroundScheduler

router = APIRouter()

# Pydanticモデルを作成
class RelaySchedule(BaseModel):
    action: str #= Field(..., regex="^(on|off)$")
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)

def tick():
    from time import sleep
    from gpiozero import LED

    relay = LED(17)

    relay.on()
    sleep(1)
    relay.off()

@router.get("/")
def get_relay_schedule( q: str = None):
    return {"schedule": "***", "q": q}

@router.post("/")
def schedule_relay_action(schedule: RelaySchedule):
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=3)
    scheduler.start()
 
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
    return {"message": f"Relay scheduled to turn {schedule.action} at {schedule.hour:02}:{schedule.minute:02} every day."}

