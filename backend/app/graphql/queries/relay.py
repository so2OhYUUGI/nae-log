# app/graphql/queries/relay.py
import strawberry
from typing import List, Optional
from app.db.session import SessionLocal
from app.entities.relay import Relay
from app.graphql.types.relay import RelayType

@strawberry.type
class RelayQuery:
    @strawberry.field
    def elays(self) -> List[RelayType]:
        with SessionLocal() as db:
            relays = db.query(Relay).all()
            return [RelayType(id=relay.id, port=relay.port, relay_type=relay.relay_type, description=relay.description, field_id=relay.field_id) for relay in relays]

    @strawberry.field
    def relay(self, id: int) -> Optional[RelayType]:
        with SessionLocal() as db:
            relay = db.query(Relay).filter(Relay.id == id).first()
            if relay:
                return RelayType(id=relay.id, port=relay.port, relay_type=relay.relay_type, description=relay.description, field_id=relay.field_id)
            return None
