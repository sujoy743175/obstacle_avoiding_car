from app.test import *
from app.HCSR_04 import HCSR04
from utime import sleep

sensor = HCSR04(32, 35)

def avoid():
    forward_distance = sensor.distance_cm()
    print(forward_distance)
    
    if forward_distance <= 5:
        forward_distance = 10
        
    if forward_distance >= 201:
        forward_distance = 200
    
    if forward_distance >= 10:
        forward()

    else:
        backward()
        turnRihgt()
    




