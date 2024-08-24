from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel

from app.core.gpio import red

router = APIRouter()

class LampState(BaseModel):
    state: Literal['on', 'off']

#####################################
# GET
#####################################
# 現在のリレーの状態を取得するエンドポイント
@router.get("/")
def lamp_status():
    # リレーがアクティブかどうかを確認し、状態を返す
    status = "on" if red.is_active else "off"
    return {"state": status}

#####################################
# POST
#####################################
@router.post("/")
def switch_lamp(state: LampState):
    if state.state == "on":
        red.on()
    elif state.state == "off":
        red.off()
    return {"lamp": state.state}
