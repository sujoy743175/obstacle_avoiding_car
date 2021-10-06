# Author: Olivier Lenoir - <olivier.len02@gmail.com>
# Created: 2020-06-14 21:05:12
# Project: Test L298 Dual H-bridge, MicroPython
# Description:

from app.l298 import LM298, RM298
from utime import sleep

def work():
    
        motorL = LM298(25, 27, 26)
        motorR = RM298(14, 13, 12)
        motorL.set_speed(500)
        motorR.set_speed(500)
        motorL.forward()
        motorR.forward()
        print('ok')
        sleep(2)
        motorL.set_speed(200)
        motorR.set_speed(200)
        motorL.forward()
        motorR.forward()
        sleep(2)
        motorL.stop()
        motorR.stop()
        motorL.reverse()
        motorR.reverse()
        sleep(2)
        motorL.stop()
        motorR.stop()       