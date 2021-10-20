from app.test import *
from app.HCSR_04 import HCSR04
from utime import sleep
from app.I2c import *

def avoid():
    forward_distance = read_distance()
    
    if forward_distance >= 10:
        forward()

    else:
        backward()
        turnRihgt()
    print(forward_distance)
    



