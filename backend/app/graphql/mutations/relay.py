# app/graphql/mutations/relay.py
import strawberry
from typing import List, Optional

from app.db.session import SessionLocal
from app.entities.relay import Relay, RelayType, RelayInput
from app.core.gpio import power_supply_relay

@strawberry.type
class RelayMutation:
    @strawberry.mutation
    def create_relay(self, input: RelayInput) -> RelayType:
        with SessionLocal() as db:
            relay = Relay(port=input.port, relay_type=input.relay_type, description=input.description, field_id=input.field_id)
            db.add(relay)
            db.commit()
            db.refresh(relay)
            return RelayType(
                id=relay.id,
                port=relay.port,
                relay_type=relay.relay_type,
                description=relay.description,
                field_id=relay.field_id,
                status=RelayMutation._get_relay_status(relay.port)
            )

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
                return RelayType(
                    id=relay.id,
                    port=relay.port,
                    relay_type=relay.relay_type,
                    description=relay.description,
                    field_id=relay.field_id,
                    status=RelayMutation._get_relay_status(relay.port)
                )
            raise ValueError(f"Relay with id {id} not found.")

    @strawberry.mutation
    def toggle_relay(self, id: int, action: Optional[str] = None) -> RelayType:
        with SessionLocal() as db:
            relay = db.query(Relay).filter(Relay.id == id).first()
            if relay:
                if action == "on":
                    power_supply_relay[relay.port].on()
                elif action == "off":
                    power_supply_relay[relay.port].off()
                else:
                    power_supply_relay[relay.port].off() if power_supply_relay[relay.port].is_active else power_supply_relay[relay.port].on()

                return RelayType(
                    id=relay.id,
                    port=relay.port,
                    relay_type=relay.relay_type,
                    description=relay.description,
                    field_id=relay.field_id,
                    status=RelayMutation._get_relay_status(relay.port)
                )
            raise ValueError(f"Relay with id {id} not found.")

    @strawberry.mutation
    def toggle_all_relays(self, action: str) -> List[RelayType]:
        statuses = []
        for i, relay in enumerate(power_supply_relay):
            if action == "on":
                relay.on()
            elif action == "off":
                relay.off()
            else:
                raise ValueError("Invalid action. Must be 'on' or 'off'.")
            statuses.append(RelayType(id=i, port=i, relay_type="", description="", field_id=0, status=action))
        return statuses

    @staticmethod
    def _get_relay_status(port: Optional[int]) -> str:
        """
        Helper method to get the status of a relay by its GPIO port.
        Handles cases where the port might be None.
        """
        if port is not None and 0 <= port < len(power_supply_relay):
            return "on" if power_supply_relay[port].is_active else "off"
        return "unknown"  # Return "unknown" if port is None or out of range
