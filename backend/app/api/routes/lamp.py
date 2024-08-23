from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LampState(BaseModel):
    state: str  # "on" または "off"

@router.post("/")
def switch_lamp(state: LampState):
    if state.state == "on":
        red.on()
    elif state.state == "off":
        red.off()
    return {"lamp": state.state}
