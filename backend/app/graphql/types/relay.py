# app/graphql/types/relay.py
import strawberry

@strawberry.type
class RelayStatus:
    id: int
    status: str
