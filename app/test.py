# Author: Olivier Lenoir - <olivier.len02@gmail.com>
# Created: 2020-06-14 21:05:12
# Project: Test L298 Dual H-bridge, MicroPython
# Description:

from app.l298 import LM298
from utime import sleep

def work():
    
        motor = LM298(2, 4, 5)
        motor.set_speed(500)
        motor.forward()
        print('ok')
        sleep(2)
        motor.set_speed(200)
        motor.forward()
        sleep(2)
        motor.stop()
        motor.reverse()
        sleep(2)
        motor.stop()

