from sqlalchemy import Column, Integer, String, DateTime
import strawberry
from pydantic import BaseModel
from datetime import datetime

from app.db.base_class import Base

# Snapshot Model (SQLAlchemy ORM Model)
class Snapshot(Base):
    __tablename__ = "snapshots"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String)
    field_id = Column(Integer, index=True)

# Pydantic Base Model
class SnapshotBase(BaseModel):
    timestamp: datetime
    file_path: str
    field_id: int

    class Config:
        from_attributes = True

class SnapshotCreate(SnapshotBase):
    pass

class SnapshotUpdate(SnapshotBase):
    pass

# Pydantic DB Schema
class SnapshotInDBBase(SnapshotBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class SnapshotSchema:
    id: int
    timestamp: datetime
    file_path: str
    field_id: int
