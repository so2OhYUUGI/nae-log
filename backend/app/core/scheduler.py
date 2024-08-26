from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from config import SQLALCHEMY_DATABASE_URL

# スケジューラのインスタンスを作成
jobstores = {
    'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URL)
}

scheduler = BackgroundScheduler(jobstores=jobstores)
