# app/graphql/types/relay.py
import strawberry
from typing import Optional

@strawberry.type
class RelayType:
    id: int
    port: int
    relay_type: str
    description: Optional[str]
    field_id: int
    status: str

@strawberry.input
class RelayInput:
    port: int
    relay_type: str
    description: Optional[str]
    field_id: int
