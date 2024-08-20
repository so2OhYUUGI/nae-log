from fastapi import APIRouter
from gpiozero import LED
from pydantic import BaseModel

router = APIRouter()

relay = LED(17)

class RelayState(BaseModel):
    state: str  # "on" または "off"

@router.get("/")
def get_lamp_status():
    # GPIOの状態を取得
    status = "on" if relay.is_active else "off"
    return {"state": status}

@router.post("/")
def switch_lamp(state: RelayState):
    if state.state == "on":
        relay.on()
    elif state.state == "off":
        relay.off()
    return {"lamp": state.state}
