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

def stop():
    motorL.stop()
    motorR.stop()
    sleep(0.05)    

def backward():
    stop()
    motorL.reverse()            
    motorR.reverse()
    sleep(.5)
    stop()   

def turnRihgt():
    print("turning right")
    print("version ........2.2.5")
    motorL.forward()
    motorR.reverse()
    sleep(0.4)
    stop()
    forward()

def turnLeft():
    print("turning left")
    motorL.reverse()
    motorR.forward()
    sleep(0.4)
    stop()
    forward()



