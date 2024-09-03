# app/db/init_db.py
# 
# $ cd backend
# $ python3 -m app.db.init_db
#
#######################################
from app.db.session import engine, SessionLocal
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

# データベース初期化とデフォルトデータの追加
def init_db():
    Base.metadata.create_all(bind=engine)
    
    # デフォルトデータを追加
    with SessionLocal() as db:
        # FIELDSテーブルにデータを追加
        if not db.query(Field).filter(Field.id == 1).first():
            field = Field(id=1, name="main", location="earth")
            db.add(field)
            db.commit()

        # RELAYSテーブルにデータを追加
        relays = [
            Relay(id=1, port=21, relay_type="light", description="supplemental lighting", field_id=1),
            Relay(id=2, port=20, relay_type="power supply", description="option", field_id=1),
            Relay(id=3, port=26, relay_type="power supply", description="option", field_id=1)
        ]

        for relay in relays:
            if not db.query(Relay).filter(Relay.id == relay.id).first():
                db.add(relay)

        db.commit()

if __name__ == "__main__":
    init_db()
