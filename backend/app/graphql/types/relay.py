import strawberry

@strawberry.type
class RelayStatus:
    id: int
    status: str
