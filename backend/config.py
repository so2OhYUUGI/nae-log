# config.py
from pathlib import Path
from dotenv import load_dotenv
import os

# .envファイルの読み込み
#env_path = Path('.') / '.env'
env_path = Path(__file__).parent / '../.env'
load_dotenv(dotenv_path=env_path)

# 環境変数から設定値を取得
PROJECT_NAME = os.getenv("PROJECT_NAME", "NaeLOG")
HOME_PATH = os.getenv("HOME_PATH", "/nae-log/")
PUBLIC_PATH = os.getenv("PUBLIC_PATH", f"{HOME_PATH}public/")
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{HOME_PATH}backend/.db/nae-log.sqlite3")