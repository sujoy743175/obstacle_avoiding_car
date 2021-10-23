# Author: Olivier Lenoir - <olivier.len02@gmail.com>
# Created: 2020-06-14 21:05:12
# Project: Test L298 Dual H-bridge, MicroPython
# Description:

from app.l298 import LM298
from utime import sleep

motorL = LM298(25, 26, 27)
motorR = LM298(14, 12, 13)
motorL.set_speed(1000)
motorR.set_speed(1000)

def forward():
    print("moving forward")
    motorL.forward()
    motorR.forward()  

def backward():
    motorL.stop()
    motorR.stop()
    sleep(0.05)
    motorL.reverse()            
    motorR.reverse()
    sleep(.5)
    motorL.stop()
    motorR.stop()

def turnRihgt():
    print("turning right")
    motorL.forward()
    motorR.reverse()
    sleep(0.4)
    motorL.stop()
    motorR.stop()
    sleep(0.05)
    motorL.forward()
    motorR.forward() 

def turnLeft():
    print("turning left")
    motorL.reverse()
    motorR.forward()
    sleep(.4)
    motorL.stop()
    motorR.stop()
    sleep(0.05)    
    motorL.forward()
    motorR.forward()
