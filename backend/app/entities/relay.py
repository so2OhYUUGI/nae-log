from sqlalchemy import Column, Integer, String
import strawberry
from pydantic import BaseModel
from typing import Optional

from app.db.base_class import Base

# Relay Model (SQLAlchemy ORM Model)
class Relay(Base):
    __tablename__ = "relays"

    id = Column(Integer, primary_key=True, index=True)
    port = Column(Integer, index=True)
    relay_type = Column(String, index=True)
    description = Column(String)
    field_id = Column(Integer, index=True)

# Pydantic Base Model
class RelayBase(BaseModel):
    port: int
    relay_type: str
    description: str
    field_id: int

    class Config:
        from_attributes = True

class RelayCreate(RelayBase):
    pass

class RelayUpdate(RelayBase):
    pass

# Pydantic DB Schema
class RelayInDBBase(RelayBase):
    id: int

# Strawberry GraphQL Schema
@strawberry.type
class RelayType:
    id: int
    port: int
    relay_type: str
    description: Optional[str]
    field_id: int
    status: Optional[str]

@strawberry.input
class RelayInput:
    port: int
    relay_type: str
    description: Optional[str]
    field_id: int
