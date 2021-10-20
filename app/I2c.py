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
    if dec == 255:
        fwd = i2c.readfrom(Arduino_add, 1)
        left = i2c.readfrom(Arduino_add, 1)
        right = i2c.readfrom(Arduino_add, 1)
        back = i2c.readfrom(Arduino_add, 1)
    
        my_fwd= int.from_bytes(fwd, "big")
        dec_fwd = float(my_fwd)
        my_left = int.from_bytes(left, "big")
        dec_left = float(my_left)
        my_right = int.from_bytes(right, "big")
        dec_right = float(my_right)
        my_back = int.from_bytes(back, "big")
        dec_back = float(my_back)
        print(dec_fwd)
        print(dec_left)
        print(dec_right)
        print(dec_back)
        
    #print(dec)
    sleep(.2)
    '''return dec
           

ij =0'''
while True:
    read_temp()
    '''
    dp=read_temp()
    print (dp)
    if dp == 255 :
        ij =0
    if ij != 0
        ij += 1
        global distVal[ij] = dp
        print(distVal)
        

            
            
    #print(val)
    #sleep(.5)
    #i2c.scan()
    '''
