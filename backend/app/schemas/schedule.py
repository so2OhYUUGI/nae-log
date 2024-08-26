from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# 共通属性
class ScheduleBase(BaseModel):
    relay_id: int
    job_id: str
    name: str
    cron: str
    active: bool = True
    next_run_time: Optional[datetime] = None

# 作成時の属性
class ScheduleCreate(ScheduleBase):
    pass

# 更新時の属性
class ScheduleUpdate(ScheduleBase):
    pass

# データベースから読み取る時の属性
class ScheduleInDBBase(ScheduleBase):
    id: int

    class Config:
        orm_mode = True

# 外部に返すスキーマ
class Schedule(ScheduleInDBBase):
    pass
