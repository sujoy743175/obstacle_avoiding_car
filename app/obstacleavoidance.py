from app.test import *
from app.HCSR_04 import HCSR04
from utime import sleep
from app.I2c import *
both_wheel_interrupt_number = 0
left_wheel_interrupt_number = 0
right_wheel_interrupt_number = 0

def avoid():
    sleep(.2) # for start_time to work properly
    global both_wheel_interrupt_number, left_wheel_interrupt_number,right_wheel_interrupt_number
    x = read_distance()
    print(x)
    distance_fwd, distance_left, distance_right, voltage, Left_Limit, Right_Limit, left_wheel_speed, right_wheel_speed = x
    threshold_distance = 25    
    volt = voltage/10

    if distance_fwd == 0:
        distance_fwd = threshold_distance 
    if distance_left == 0:
        distance_left = threshold_distance 
    if distance_right == 0:
        distance_right = threshold_distance
           
    #sleep(0.05)
            
    
    if distance_fwd >= threshold_distance and (Left_Limit == 1 and Right_Limit == 1): # and (left_wheel_speed != 0 or right_wheel_speed != 0):
        forward()
        #print("forward")    
    if both_wheel_interrupt_number == 10 and distance_left > distance_right:
        print("........both wheel stopped")
        backward()
        turnLeft()

    if left_wheel_interrupt_number == 10:
        print("........left wheel stopped")
        backward()
        turnLeft()
    
    if right_wheel_interrupt_number == 10:
        print("........right wheel stopped")
        backward()
        turnRihgt()
    if both_wheel_interrupt_number == 10 and distance_left < distance_right:
        print("........both wheel stopped")
        backward()
        turnRihgt()
    if both_wheel_interrupt_number == 10 and distance_left == distance_right:
        print("........both wheel stopped")
        backward()
        turnRihgt()
    if Left_Limit == 0 and  Right_Limit == 1:
        print("........Left limit")
        backward()
        turnRihgt()      
    if Left_Limit == 1 and  Right_Limit == 0:
        print("........Right limit")
        backward()
        turnLeft()   
    if Left_Limit == 0 and  Right_Limit == 0:
        print("........Both limits")
        backward()
        turnLeft()     

    if left_wheel_speed == 0.0 and  right_wheel_speed == 0.0 and both_wheel_interrupt_number >=10:
        print("........resetting both_wheel_interrupt_number ")    
        both_wheel_interrupt_number = 0

    if left_wheel_speed == 0.0 and  left_wheel_interrupt_number >=10:
        print("........resetting left_wheel_interrupt_number ")    
        left_wheel_interrupt_number = 0

    if right_wheel_speed == 0.0 and  right_wheel_interrupt_number >=10:
        print("........resetting left_wheel_interrupt_number ")    
        right_wheel_interrupt_number = 0

    if left_wheel_speed == 0 and  right_wheel_speed == 0:
        both_wheel_interrupt_number = both_wheel_interrupt_number + 1 
        print ("both_wheel_interrupt_number")
        print (both_wheel_interrupt_number)
    
    if left_wheel_speed == 0:
        left_wheel_interrupt_number = left_wheel_interrupt_number + 1 
        print ("left_wheel_interrupt_number")
        print (left_wheel_interrupt_number)

    if right_wheel_speed == 0:
        right_wheel_interrupt_number = right_wheel_interrupt_number + 1 
        print ("left_wheel_interrupt_number")
        print (right_wheel_interrupt_number)
        
    if (left_wheel_speed != 0 or  right_wheel_speed != 0)or (left_wheel_speed != 0 and right_wheel_speed != 0):
        both_wheel_interrupt_number = 0
    
    if left_wheel_speed != 0:
        left_wheel_interrupt_number = 0

    if right_wheel_speed != 0:
        right_wheel_interrupt_number = 0
       
    if distance_fwd < threshold_distance and distance_left > distance_right:
        #print("going left")
        backward()
        turnLeft()        
    if distance_fwd < threshold_distance and distance_left < distance_right:
        #print("going right")
        backward()
        turnRihgt()
    if distance_fwd < threshold_distance and distance_left == distance_right:
        #print("going right")
        backward()
        turnRihgt()        
    
    '''print ("Left speed ... alias...left_wheel_speed")
    print(left_wheel_speed)
    print ("Right speed ... alias...right_wheel_speed")
    print(right_wheel_speed)'''
    print ("voltage........................")
    print(volt)
