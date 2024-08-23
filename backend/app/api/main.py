from fastapi import APIRouter

from app.api.routes import lamp, relay, relay_schedule

api_router = APIRouter()
api_router.include_router(lamp.router, prefix="/lamp", tags=["lamp"])
api_router.include_router(relay.router, prefix="/relay", tags=["relay"])
api_router.include_router(relay_schedule.router, prefix="/relay/schedule", tags=["relay schedule"])
