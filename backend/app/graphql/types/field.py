import strawberry
from typing import Optional
from datetime import datetime

@strawberry.type
class FieldType:
    id: int
    name: str
    location: Optional[str]
    created_at: datetime

@strawberry.input
class FieldInput:
    name: str
    location: Optional[str]
