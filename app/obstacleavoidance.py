from app.test import *
from app.HCSR_04 import HCSR04
from utime import sleep
from app.I2c import *

def avoid():
    x = read_distance()    
    distance_fwd, distance_left, distance_right, distance_back = x
    y = distance_back
    sleep(.3)

    

    if distance_fwd >= 10:
        forward()

    elif distance_fwd <10 and distance_left > distance_right:
        backward()
        turnLeft()
    elif distance_fwd < 10 and distance_left < distance_right:
        backward()
        turnRihgt
    elif distance_fwd < 10 and distance_left == distance_right:
        backward()
        turnRihgt()

  
    



