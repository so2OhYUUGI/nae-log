from fastapi import APIRouter
from gpiozero import LED

router = APIRouter()

red = LED(4)

@router.get("/{is_on}")
def read_item(is_on: str, q: str = None):
    if is_on == "on":
        red.on()
    else:
        red.off()
    return {"lamp": is_on, "q": q}
