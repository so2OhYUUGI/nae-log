from fastapi import APIRouter
from gpiozero import LED
from pydantic import BaseModel

from app.core.gpio import power_supply_relay

router = APIRouter()

# リレーの状態を表すPydanticモデルを定義
class RelayState(BaseModel):
    state: str  # "on" または "off"

#####################################
# GET
#####################################
# 現在のリレーの状態を取得するエンドポイント
@router.get("/")
def relay_status():
    # リレーがアクティブかどうかを確認し、状態を返す
    status = "on" if power_supply_relay[0].is_active else "off"
    return {"state": status}

# 特定のリレーの状態を取得するエンドポイント
@router.get("/{relay_id}")
def relay_status(relay_id: int, q: str = None):
    # 指定されたリレーIDの状態を確認し、状態を返す
    status = "on" if power_supply_relay[relay_id].is_active else "off"
    return {"state": status, "id": relay_id}

#####################################
# POST
#####################################
# リレーをオンまたはオフに切り替えるエンドポイント
@router.post("/")
def switch_relay(state: RelayState):
    # 送信された状態に基づいてリレーを操作
    if state.state == "on":
        power_supply_relay[0].on()
    elif state.state == "off":
        power_supply_relay[0].off()
    
    # 操作後のリレーの状態を確認し、返す
    status = "on" if power_supply_relay[0].is_active else "off"
    return {"state": status}

# 特定のリレーをオンまたはオフに切り替えるエンドポイント
@router.post("/{relay_id}")
def switch_relay(state: RelayState, relay_id: int):
    # 指定されたリレーIDの状態に基づいてリレーを操作
    if state.state == "on":
        power_supply_relay[relay_id].on()
    elif state.state == "off":
        power_supply_relay[relay_id].off()
    
    # 操作後のリレーの状態を確認し、返す
    status = "on" if power_supply_relay[relay_id].is_active else "off"
    return {"state": status, "id": relay_id}
