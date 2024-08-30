# app/graphql/queries/relay_status.py
import strawberry
from typing import List, Optional

from app.core.gpio import power_supply_relay
from app.graphql.types.relay import RelayStatus

@strawberry.type
class RelayStatusQuery:
    @strawberry.field
    def relay_status(self, id: Optional[int] = None) -> List[RelayStatus]:
        if id is not None:
            return [RelayStatus(id=id, status="on" if power_supply_relay[id].is_active else "off")]
        else:
            return [RelayStatus(id=i, status="on" if r.is_active else "off") for i, r in enumerate(power_supply_relay)]
