# app/api/routes/relay_schedule/__init__.py
from fastapi import APIRouter

from .get_relay_schedule import router as get_router
from .post_relay_schedule import router as post_router

router = APIRouter()
router.include_router(get_router)
router.include_router(post_router)