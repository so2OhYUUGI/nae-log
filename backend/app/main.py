# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.gpio import server_run_led
from app.core.scheduler import scheduler
from app.db.session import SessionLocal
from app.entities.automation_schedule import AutomationScheduleBase
from app.utils.relay_utils import get_relay_action  # 追加: get_relay_actionを使用
from config import PUBLIC_PATH
from app.restapi.main import api_router
from app.graphql.main import graphql_app
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    server_run_led.on()  # サーバー起動時にLEDを点灯
    scheduler.start()    # APSchedulerを開始

    # データベースからスケジュールを復元
    session = SessionLocal()
    try:
        schedules = session.query(AutomationScheduleBase).all()
        for schedule in schedules:
            if schedule.active:
                # アクションを取得（on/off アクションに基づいて）
                job_function = get_relay_action(schedule.action)
                
                # スケジュールを復元
                scheduler.add_job(
                    job_function,  # 追加: アクション関数を渡す
                    trigger='cron',
                    cron=schedule.cron,
                    id=schedule.job_id,
                    name=schedule.name,
                    next_run_time=schedule.next_run_time or 'now',
                    args=[schedule.relay_id]  # リレーIDをアクションに渡す
                )
                print(f"Restored schedule: {schedule.name}")
    except Exception as e:
        print(f"Error loading schedules: {e}")
    finally:
        session.close()

    print('###***--- naelog server start ---***###')
    yield
    server_run_led.off()  # サーバー終了時にLEDを消灯
    print('###***--- naelog server shutdown ---***###')


def custom_generate_unique_id(route):
    return f"{route.tags[0]}-{route.name}"

app = FastAPI(
    title="NaeLOG",
    openapi_url=f"/localhost:8000/openapi.json",
    generate_unique_id_function=custom_generate_unique_id,
    lifespan=lifespan,
)

# CORS設定
origins = [
    "http://localhost:8000",  # 本番環境では削除
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# APIルーターとGraphQLルーターを追加
app.include_router(api_router, prefix="/api")
app.include_router(graphql_app, prefix="/graphql", tags=["graphql"])

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
