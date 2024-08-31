# app/db/init_db.py
# 
# $ cd backend
# $ python3 -m app.db.init_db
from app.db.session import engine
from app.db.base_class import Base
from app.entities.schedule import Schedule

# データベース初期化
def init_db():
    Base.metadata.create_all(bind=engine)  
    Schedule.metadata.create_all(bind=engine) # Scheduleのmetadataを使用してテーブルを作成

if __name__ == "__main__":
    init_db()
