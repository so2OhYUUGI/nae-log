from config import PUBLIC_PATH

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from crontab import CronTab

router = APIRouter()

# Pydanticモデルを作成
class RelaySchedule(BaseModel):
    action: str = Field(..., regex="^(on|off)$")
    hour: int = Field(..., ge=0, le=23)
    minute: int = Field(..., ge=0, le=59)

@router.get("/")
def get_relay_schedule(schedule: RelaySchedule):
    return "test"

@router.post("/")
def schedule_relay_action(schedule: RelaySchedule):
    # コマンド設定
    command = f'{PUBLIC_PATH}../.venv/bin/python3 {PUBLIC_PATH}/bin/{schedule.action}-relay.py'

    # Crontabのインスタンスを作成
    cron = CronTab(user=True)

    # 新しいジョブを作成
    job = cron.new(command=command, comment=f"Relay {schedule.action.capitalize()} Job")

    # 指定された時間で毎日実行するように設定
    job.minute.on(schedule.minute)
    job.hour.on(schedule.hour)
    job.every().day()

    # Crontabを更新して保存
    cron.write()

    return {"message": f"Relay scheduled to turn {schedule.action} at {schedule.hour:02}:{schedule.minute:02} every day."}

# その他のエラーハンドリング
@router.exception_handler(Exception)
def handle_exception(exc: Exception):
    raise HTTPException(status_code=500, detail=str(exc))
