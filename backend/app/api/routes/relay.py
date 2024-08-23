from fastapi import APIRouter
from gpiozero import LED
from pydantic import BaseModel

from app.core.gpio import power_supply_relay

router = APIRouter()


class RelayState(BaseModel):
    state: str  # "on" または "off"

@router.get("/")
def relay_status():
    # GPIOの状態を取得
    status = "on" if power_supply_relay[0].is_active else "off"
    return {"state": status}

@router.post("/")
def switch_relay(state: RelayState):
    if state.state == "on":
        power_supply_relay[0].on()
    elif state.state == "off":
        power_supply_relay[0].off()
    status = "on" if power_supply_relay[0].is_active else "off"
    return {"state": status}
