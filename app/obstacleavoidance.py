from app.test import *
from app.HCSR_04 import HCSR04
from utime import sleep
from app.I2c import *

def avoid():
    x = read_distance()
    print(x)
    distance_fwd, distance_left, distance_right = x
    threshold_distance = 15    
       

    if distance_fwd == 0:
        distance_fwd = threshold_distance 

    if distance_left == 0:
        distance_left = threshold_distance 

    if distance_right == 0:
        distance_right = threshold_distance
        
    print (distance_fwd)
    print(distance_left)
    print(distance_right)
    sleep(0.05)
            
    
    if distance_fwd >= threshold_distance:
        forward()
        #print("forward")

    elif distance_fwd < threshold_distance and distance_left > distance_right:
        #print("going left")
        backward()
        turnLeft()
        
    elif distance_fwd < threshold_distance and distance_left < distance_right:
        #print("going right")
        backward()
        turnRihgt()
    elif distance_fwd < threshold_distance and distance_left == distance_right:
        #print("going right")
        backward()
        turnRihgt()

  

