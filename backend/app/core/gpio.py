from gpiozero import LED

# App server run led
# pin no, 7
server_run_led = LED(4)

# gpio control
# pin no, 11
red = LED(17)

# Power Supply Relay Control
# pin no(gpio no), 40(21), 38(20), 37(26)
power_supply_relay = [
	None, None, None, None, None, None, None, None, None, None, # 0-9
	None, None, None, None, None, None, None, None, None, None, # 10-19
	LED(20), LED(21), None, None, None, None, LED(26), None, None, None, # 20-29
]
