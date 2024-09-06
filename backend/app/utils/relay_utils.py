# app/util/relay_util.py
from typing import Callable
from app.db.session import SessionLocal
from app.entities.relay import Relay
from app.core.gpio import power_supply_relay

def get_port_by_relay_id(relay_id: int) -> int:
    """
    リレーIDに基づいてポート番号を取得する。
    """
    with SessionLocal() as db:
        relay = db.query(Relay).filter(Relay.id == relay_id).first()
        if relay:
            return relay.port
        else:
            raise ValueError(f"No port mapping found for relay ID {relay_id}.")

def get_relay_action(action: str) -> Callable[[int], None]:
    """
    リレーのon/offアクションを返す関数。
    """
    if action == "on":
        return _on_relay
    elif action == "off":
        return _off_relay
    else:
        raise ValueError(f"Invalid action: {action}")

def _on_relay(relay_id: int):
    """
    指定されたリレーIDのリレーをオンにするアクション。
    """
    port = get_port_by_relay_id(relay_id)
    if 0 <= port < len(power_supply_relay):
        relay = power_supply_relay[port]
        relay.on()
    else:
        print(f"Relay with port {port} is not found or not initialized.")

def _off_relay(relay_id: int):
    """
    指定されたリレーIDのリレーをオフにするアクション。
    """
    port = get_port_by_relay_id(relay_id)
    if 0 <= port < len(power_supply_relay):
        relay = power_supply_relay[port]
        relay.off()
    else:
        print(f"Relay with port {port} is not found or not initialized.")
