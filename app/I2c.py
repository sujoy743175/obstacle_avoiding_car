from app.start import *
from app.connect_and_update import connectToWifiAndUpdate

connectToWifiAndUpdate()

import machine
import sys
from utime import sleep
from machine import Pin

led_builtin = Pin(2, Pin.OUT)


sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)

# Create an I2C object out of our SDA and SCL pin objects
i2c = machine.I2C(1, sda=sda_pin, scl=scl_pin, freq = 400000)

# TMP102 address on the I2C bus
Arduino_add = 8


def read_temp():

    # Read temperature registers
    val = i2c.readfrom(Arduino_add, 1)
    #temp_c = (val[0] << 4) | (val[1] >> 5)

    #return val

    #print(val)
    my_str= int.from_bytes(val, "big")
    #int_val = int.from_bytes(val, byteorder=sys.byteorder)
    #my_str = str(val)
    dec = float(my_str)
    print(dec)
    sleep(1)
    if dec <=10:
        led_builtin.value(0)
    else:
        led_builtin.value(1)


while True:
    read_temp()
    

            
            
    #print(val)
    #sleep(.5)
    #i2c.scan()
    

   


    
    




