from fastapi import APIRouter
from gpiozero import LED

router = APIRouter()
relay = LED(17)

@router.get("/{is_on}")
def read_item(is_on: str, q: str = None):
    if is_on == "on":
        relay.on()
    else:
        relay.off()
    return {"relay": is_on, "q": q}
