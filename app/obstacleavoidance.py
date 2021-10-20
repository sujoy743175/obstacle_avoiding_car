from app.test import *
from app.HCSR_04 import HCSR04
from utime import sleep

sensor = HCSR04(32, 35)

def avoid():
    forward_distance = sensor.distance_cm()
    if forward_distance >= 10:
        forward()

    else:
        backward()
        turnRihgt()
    



