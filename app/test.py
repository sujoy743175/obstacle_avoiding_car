# Author: Olivier Lenoir - <olivier.len02@gmail.com>
# Created: 2020-06-14 21:05:12
# Project: Test L298 Dual H-bridge, MicroPython
# Description:

from app.l298 import LM298
from utime import sleep

motorL = LM298(25, 27, 26)
motorR = LM298(14, 13, 12)
motorL.set_speed(1000)
motorR.set_speed(1000)

def forward():
    motorL.forward()
    motorR.forward()  

def backward():
    motorL.stop()
    motorR.stop()
    sleep(0.5)
    motorL.reverse()            
    motorR.reverse()
    sleep(0.5)
    motorL.stop()
    motorR.stop()

def turnRihgt():
    motorL.forward()
    motorR.reverse()
    sleep(0.5)
    motorL.forward()
    motorR.forward() 

def turnLeft():
    motorL.reverse()
    motorR.forward()
    sleep(0.5)
    motorL.forward()
    motorR.forward()
    
def work():
    turnRihgt()

    
    
    




