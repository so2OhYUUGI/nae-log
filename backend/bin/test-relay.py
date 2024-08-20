from gpiozero import LED
import time

relay = LED(17)

relay.on()
time.sleep(3)
relay.off()

print(f"Job scheduled to run")
