from machine import Pin
import time

onboardLED = Pin(25, Pin.OUT)
onboardLED.value(1)
val = 1
while True:
    if val == 1:
        val = 0
    else:
        val = 1
    onboardLED.value(val)
    time.sleep(1)

