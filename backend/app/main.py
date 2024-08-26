from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.core.gpio import server_run_led
from app.core.scheduler import scheduler

from app.api.main import api_router
from app.graphql.main import graphql_app

from app.core.scheduler import scheduler
from app.db.session import SessionLocal
from app.models.schedule import Schedule

from config import PUBLIC_PATH


@asynccontextmanager
async def lifespan(app: FastAPI):
    server_run_led.on()  # サーバー起動時にLEDを点灯
    scheduler.start()    # APSchedulerを開始

    # データベースからスケジュールを復元
    session = SessionLocal()
    schedules = session.query(Schedule).all()
    for schedule in schedules:
        if schedule.active:
            # スケジュールを復帰
            scheduler.add_job(
                id=schedule.job_id,
                name=schedule.name,
                trigger='cron',
                cron=schedule.cron,
                next_run_time=schedule.next_run_time,
            )

    print('###***--- naelog server start ---***###')
    yield
    server_run_led.off()  # サーバー終了時にLEDを消灯
    print('###***--- naelog server shutdown ---***###')

def custom_generate_unique_id(route: APIRoute) -> str:
    return f"{route.tags[0]}-{route.name}"

app = FastAPI(
    title="NaeLOG",
    openapi_url=f"/localhost:8000/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan,
)

origins = [
    "http://localhost:8000",  # 本番環境時は削除してください
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# APIルーターとGraphQLルーターの追加
app.include_router(api_router, prefix="/api")
app.include_router(graphql_app, prefix="/graphql", tags=["graphql"])

#app.add_route("/graphql", graphql_app)
#app.add_websocket_route("/graphql", graphql_app)

app.mount("/app", StaticFiles(directory=PUBLIC_PATH, html=True), name="app")

# for api error log
'''
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
@app.exception_handler(RequestValidationError)
async def handler(request:Request, exc:RequestValidationError):
    print(exc)
    return JSONResponse(content={}, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
'''
