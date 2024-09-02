# app/db/init_db.py
# 
# $ cd backend
# $ python3 -m app.db.init_db
#
#######################################
from app.db.session import engine
from app.db.base_class import Base
from app.entities.field import Field
from app.entities.camera_stream import CameraStream
from app.entities.sensor import Sensor
from app.entities.relay import Relay
from app.entities.environmental_data import EnvironmentalData
from app.entities.automation_schedule import AutomationSchedule
from app.entities.notification_schedule import NotificationSchedule
from app.entities.plant import Plant
from app.entities.snapshot import Snapshot
from app.entities.observation import Observation

from app.entities.schedule import Schedule ## 廃止予定

# データベース初期化
def init_db():
    Base.metadata.create_all(bind=engine)  

if __name__ == "__main__":
    init_db()
