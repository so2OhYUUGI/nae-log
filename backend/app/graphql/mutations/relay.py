# app/graphql/mutations/relay.py
import strawberry
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.entities.relay import Relay, RelayType, RelayInput

@strawberry.type
class RelayMutation:
    @strawberry.mutation
    def create_relay(self, input: RelayInput) -> RelayType:
        with SessionLocal() as db:
            relay = Relay(port=input.port, relay_type=input.relay_type, description=input.description, field_id=input.field_id)
            db.add(relay)
            db.commit()
            db.refresh(relay)
            return RelayType(id=relay.id, port=relay.port, relay_type=relay.relay_type, description=relay.description, field_id=relay.field_id)

    @strawberry.mutation
    def update_relay(self, id: int, input: RelayInput) -> RelayType:
        with SessionLocal() as db:
            relay = db.query(Relay).filter(Relay.id == id).first()
            if relay:
                relay.port = input.port
                relay.relay_type = input.relay_type
                relay.description = input.description
                relay.field_id = input.field_id
                db.commit()
                db.refresh(relay)
                return RelayType(id=relay.id, port=relay.port, relay_type=relay.relay_type, description=relay.description, field_id=relay.field_id)
            raise ValueError(f"Relay with id {id} not found.")
