from machine import Pin, PWM
pin_motor = machine.Pin(4, machine.Pin.OUT)
pwm_motor = machine.PWM(pin_motor)
pin_motor_a = machine.Pin(4, machine.Pin.OUT)
pin_motor_b = machine.Pin(5, machine.Pin.OUT)