# app/graphql/queries/relay.py
import strawberry
from typing import List, Optional
from app.db.session import SessionLocal
from app.entities.relay import Relay, RelayType
from app.core.gpio import power_supply_relay

@strawberry.type
class RelayQuery:
    @strawberry.field
    def relays(self) -> List[RelayType]:
        with SessionLocal() as db:
            relays = db.query(Relay).all()
            return [
                RelayType(
                    id=relay.id,
                    port=relay.port,
                    relay_type=relay.relay_type,
                    description=relay.description,
                    field_id=relay.field_id,
                    status=RelayQuery._get_relay_status(relay.port)
                )
                for relay in relays
            ]

    @strawberry.field
    def relay(self, id: int) -> Optional[RelayType]:
        with SessionLocal() as db:
            relay = db.query(Relay).filter(Relay.id == id).first()
            if relay:
                return RelayType(
                    id=relay.id,
                    port=relay.port,
                    relay_type=relay.relay_type,
                    description=relay.description,
                    field_id=relay.field_id,
                    status=RelayQuery._get_relay_status(relay.port)
                )
            return None

    @staticmethod
    def _get_relay_status(port: Optional[int]) -> str:
        """
        Helper method to get the status of a relay by its GPIO port.
        Handles cases where the port might be None.
        """
        if port is not None and 0 <= port < len(power_supply_relay):
            return "on" if power_supply_relay[port].is_active else "off"
        return "unknown"  # Return "unknown" if port is None or out of range
