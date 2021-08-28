from machine import Pin, PWM
from app.HCSR_04 import *


import time
#import utime

inputPin = Pin(2, Pin.IN)
inputPinR = Pin(33, Pin.IN)
motorLPin1 = Pin(27, Pin.OUT)
motorLPin2 = Pin(26, Pin.OUT)
enableLPin = PWM(Pin(25), freq=300, duty=1000) # freq = 300 may give better speed
motorRPin1 = Pin(13, Pin.OUT)
motorRPin2 = Pin(12, Pin.OUT)
enableRPin = PWM(Pin(14), freq=300, duty=650)

#enableLPin.duty_u16(65025)
#enableRPin.duty_u16(65025)

def move_forward():
    motorLPin1.off()
    motorLPin2.on()
    motorRPin1.off()
    motorRPin2.on()

def move_backward():
    motorLPin1.on()
    motorLPin2.off()
    motorRPin1.on()
    motorRPin2.off()

def move_stop():
    motorLPin1.off()
    motorLPin2.off()
    motorRPin1.off()
    motorRPin2.off()

def turn_right():
    motorLPin1.on()
    motorLPin2.off()
    motorRPin1.off()
    motorRPin2.on()
    time.sleep(0.5)
    move_stop()
    move_forward()       

def turn_left():
    motorLPin1.off()
    motorLPin2.on()
    motorRPin1.on()
    motorRPin2.off()
    time.sleep(0.5)
    move_stop()
    move_forward()
    
    
def avoid():
    
    while True:

        distance_cm()
        
        if (inputPin.value() == 1 and inputPinR.value() == 1):
            move_forward()
            #print("moving forward")
            
        elif (inputPin.value() == 1 and inputPinR.value() == 0):
            move_stop()
            print("moving stop")
            time.sleep(0.5)
            move_backward()
            print("moving backward")
            time.sleep(1)    
            move_stop()
            print("moving stop")
            time.sleep(0.5)
            turn_left()
            print("moving left")

        elif (inputPin.value() == 0 and inputPinR.value() == 1):
            move_stop()
            print("moving stop")
            time.sleep(0.5)
            move_backward()
            print("moving backward")
            time.sleep(1)    
            move_stop()
            print("moving stop")
            time.sleep(0.5)
            turn_right()    
            print("moving right")

        elif (inputPin.value() == 0 and inputPinR.value() == 0):
            move_stop()
            print("moving stop")
            time.sleep(0.5)
            move_backward()
            print("moving backward")
            time.sleep(1)    
            move_stop()
            print("moving stop")
            turn_right()    
            print("moving right") 
            



