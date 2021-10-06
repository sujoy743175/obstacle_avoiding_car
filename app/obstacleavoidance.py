from app.test import *
from app.HCSR_04 import HCSR04

sensor = HCSR04(23, 24)

def avoid():
    forward_distance = sensor.distance_cm()
    if forward_distance >= 10:
        forward()

    else:
        turnRihgt()


