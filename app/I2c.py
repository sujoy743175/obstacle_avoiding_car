import machine
import sys
from utime import sleep

sda_pin = machine.Pin(21)
scl_pin = machine.Pin(22)

# Create an I2C object out of our SDA and SCL pin objects
i2c = machine.I2C(1, sda=sda_pin, scl=scl_pin, freq = 400000)

Arduino_add = 8
def read_distance():    
    val = i2c.readfrom(Arduino_add, 1)    
    my_str= int.from_bytes(val, "big")    
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
    sleep(.2)