import machine
import sys
from utime import sleep

sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)

# Create an I2C object out of our SDA and SCL pin objects
i2c = machine.I2C(1, sda=sda_pin, scl=scl_pin, freq = 400000)

Arduino_add = 8

def read_distance():
    #sleep(.30)    
    byte_val = i2c.readfrom(Arduino_add, 1)    
    float_val= int.from_bytes(byte_val, "big")    
    decimal_val = float(float_val)
    if decimal_val == 255:
        fwd = i2c.readfrom(Arduino_add, 1)
        left = i2c.readfrom(Arduino_add, 1)
        right = i2c.readfrom(Arduino_add, 1)
        back = i2c.readfrom(Arduino_add, 1)
        leftLimit = i2c.readfrom(Arduino_add, 1)
        rightLimit = i2c.readfrom(Arduino_add, 1)
        leftDistance = i2c.readfrom(Arduino_add, 1)
        rightDistance = i2c.readfrom(Arduino_add, 1)

        distance_fwd = int.from_bytes(fwd, "big" )
        distance_forward = float(distance_fwd)

        distance_lft = int.from_bytes(left, "big" )
        distance_left = float(distance_lft)

        distance_rt = int.from_bytes(right, "big" )
        distance_right = float(distance_rt)
        
        limit_left = int.from_bytes(leftLimit, "big" )
        Left_Limit = float(limit_left)
        
        limit_right = int.from_bytes(rightLimit, "big" )
        Right_Limit = float(limit_right)
       
        Left_distance = int.from_bytes(leftDistance, "big" )
        Left_Distancee = float(Left_distance)
        
        Right_distance = int.from_bytes(rightDistance, "big" )
        Right_Distancee = float(Right_distance)

        return distance_forward, distance_left, distance_right, Left_Limit, Right_Limit, Left_Distancee, Right_Distancee
    
        '''print(distance_forward)
        print(distance_left)
        print(distance_right)
        print(Left_Limit)
        print(Right_Limit)
        print ("left distance")
        print(Left_Distancee)
        print ("right distance")
        print(Right_Distancee)'''


