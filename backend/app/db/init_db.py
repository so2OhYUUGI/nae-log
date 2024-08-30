# $ cd backend
# $ python3 -m app.db.init_db
from app.db.session import engine
from app.entities.schedule import Schedule  # リファクタリングに合わせてインポート先を変更

# データベース初期化
def init_db():
    Schedule.metadata.create_all(bind=engine)  # Scheduleのmetadataを使用してテーブルを作成

if __name__ == "__main__":
    init_db()
