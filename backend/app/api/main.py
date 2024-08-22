from fastapi import APIRouter

from app.api.routes import items, lamp, relay, relayTimer

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(lamp.router, prefix="/lamp", tags=["lamp"])
api_router.include_router(relay.router, prefix="/relay", tags=["relay"])
api_router.include_router(relayTimer.router, prefix="/relay/schedule", tags=["relay"])
