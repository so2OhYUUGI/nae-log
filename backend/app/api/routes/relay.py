from fastapi import APIRouter
from gpiozero import LED
from pydantic import BaseModel

from app.core.gpio import relay

router = APIRouter()


class RelayState(BaseModel):
    state: str  # "on" または "off"

@router.get("/")
def relay_status():
    # GPIOの状態を取得
    status = "on" if relay.is_active else "off"
    return {"state": status}

@router.post("/")
def switch_relay(state: RelayState):
    if state.state == "on":
        relay.on()
    elif state.state == "off":
        relay.off()
    status = "on" if relay.is_active else "off"
    return {"state": status}
