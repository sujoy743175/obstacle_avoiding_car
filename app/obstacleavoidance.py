from app.test import *
from app.HCSR_04 import HCSR04
from utime import sleep
from app.I2c import *

def avoid():
    x = read_distance()
    #print(x)
    distance_fwd, distance_left, distance_right, Left_Limit, Right_Limit  = x
    threshold_distance = 15    
       

    if distance_fwd == 0:
        distance_fwd = threshold_distance 

    if distance_left == 0:
        distance_left = threshold_distance 

    if distance_right == 0:
        distance_right = threshold_distance
        
    '''print (distance_fwd)
    print(distance_left)
    print(distance_right)'''
    #sleep(0.05)
            
    
    if distance_fwd >= threshold_distance and Left_Limit == 1 and Right_Limit == 1:
        forward()
        #print("forward")
    
    if Left_Limit == 0 and  Right_Limit == 1:
        backward()
        turnRihgt()
        print("........Left limit")
        
    if Left_Limit == 1 and  Right_Limit == 0:
        backward()
        turnLeft()
        print("........Right limit")
    
    if Left_Limit == 0 and  Right_Limit == 0:
        backward()
        turnLeft()
        print("........Both limits")
        
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

  




