# $ cd backend
# $ python3 -m app.db.init_db
from app.db.session import engine
from app.models import schedule

# データベース初期化
def init_db():
    schedule.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
