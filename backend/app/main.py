#import sentry_sdk
from config import PUBLIC_PATH

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.routing import APIRoute
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.main import api_router

from app.core.gpio import server_run_led

@asynccontextmanager
async def lifespan(app: FastAPI):
    server_run_led.on()
    print('naelog server start')
    yield
    server_run_led.off()
    print('naelog server shutdown')

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"

app = FastAPI(
    title="NaeLOG",
    openapi_url=f"/localhost:8000/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan,
)

origins = [
    # 本番環境時は削除してください
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api")
app.mount("/app", StaticFiles(directory=PUBLIC_PATH, html=True), name="app")
