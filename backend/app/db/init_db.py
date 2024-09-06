# app/db/init_db.py
# 
# $ cd backend
# $ python3 -m app.db.init_db --recreate  # 既存データを削除して再作成
# $ python3 -m app.db.init_db             # 既存データを保持
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

def init_db(recreate: bool = False):
    """
    データベースの初期化を行う関数。
    recreate: True の場合、既存のデータを削除して再作成。

    データベース用のフォルダがないときはsqlite3ファイルの作成に失敗する。要対応
    """
    if recreate:
        Base.metadata.drop_all(bind=engine)  # 既存のテーブルを削除
        print("データベースを再作成します...")
    
    Base.metadata.create_all(bind=engine)  # テーブルの作成

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

        # AUTOMATION_SCHEDULESテーブルにデータを追加 (朝6:10にON, 夕方18:30にOFF)
        schedules = [
            AutomationSchedule(
                relay_id=1,
                job_id="morning_on",
                name="Morning On",
                cron="10 6 * * *",  # 毎日6:10に実行
                active=True,
                action="on",
                next_run_time=None
            ),
            AutomationSchedule(
                relay_id=1,
                job_id="evening_off",
                name="Evening Off",
                cron="30 18 * * *",  # 毎日18:30に実行
                active=True,
                action="off",
                next_run_time=None
            )
        ]

        for schedule in schedules:
            if not db.query(AutomationSchedule).filter(AutomationSchedule.job_id == schedule.job_id).first():
                db.add(schedule)

        db.commit()

if __name__ == "__main__":
    import argparse

    # コマンドライン引数で「recreate」オプションを指定できるようにする
    parser = argparse.ArgumentParser(description="Initialize the database.")
    parser.add_argument('--recreate', action='store_true', help='Recreate the database (drop and create tables).')
    args = parser.parse_args()

    init_db(recreate=args.recreate)
