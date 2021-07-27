from machine import Pin
import time

led_builtin = Pin(2, Pin.OUT)



def blink():
    while True:
        led_builtin.value(not led_builtin.value())
        time.sleep_ms(1000)
        
    # led_builtin.value(1)
    # print('led on ...!')
    # time.sleep(1)
    # led_builtin.value(0)
    # print('led off ...!')
    # time.sleep(1)
    
    

