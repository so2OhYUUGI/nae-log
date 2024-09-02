# app/graphql/mutations/relay_status.py
import strawberry
from typing import List, Optional
from app.core.gpio import power_supply_relay
from app.graphql.types.relay import RelayType

@strawberry.type
class RelayTypeMutation:
    @strawberry.mutation
    def toggle_relay(self, id: int, action: Optional[str] = None) -> RelayType:
        if action is not None:
            if action == "on":
                power_supply_relay[id].on()
            elif action == "off":
                power_supply_relay[id].off()
        else:
            power_supply_relay[id].off() if power_supply_relay[id].is_active else power_supply_relay[id].on()

        return RelayType(id=id, status="on" if power_supply_relay[id].is_active else "off")

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
            statuses.append(RelayType(id=i, status=action))

        return statuses
