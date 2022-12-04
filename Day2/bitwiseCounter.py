# Imports
from machine import Pin
import time

#Set up our LED names and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

REDFLAG = 1
AMBERFLAG = 1 << 1
GREENFLAG = 1 << 2

counter = 0

while True:
    counter %= 8

    red.value(counter & REDFLAG)
    amber.value(counter & AMBERFLAG)
    green.value(counter & GREENFLAG)

    time.sleep(0.5)
    counter += 1