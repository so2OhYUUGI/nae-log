from fastapi import APIRouter

from app.api.routes import items, lamp, relay, relay_timer

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(lamp.router, prefix="/lamp", tags=["lamp"])
api_router.include_router(relay.router, prefix="/relay", tags=["relay"])
api_router.include_router(relay_timer.router, prefix="/schedule", tags=["relay/schedule"])