import machine, time
from machine import Pin

class HCSR04:
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        self.echo_timeout_us = echo_timeout_us
        #init trigger pin(out)
        self.trigger = Pin(trigger_pin, mode = Pin.OUT, pull=None)
        self.trigger.value(0)

        #init echo pin(in)
        self.echo = Pin(echo_pin, mode = Pin.IN, pull=None)

    def _send_puse_and_wait(self):
        '''
        Send the pulse to trigger and listen on echo pin.
        We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.
        '''
        self.trigger.value(0)  # Stabilize  the sensor
        time.sleep_us(5)
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110: # 110 = TIMEDOUT
                raise OSError('out of range')
            raise ex

    def distance_mm(self):
        pulse_time = self._send_puse_and_wait()
        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.34320 cm/us that is 1mm each 2.91us
        # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582 
        mm = pulse_time * 100 // 582  # // means return only int
        return mm

    def distance_cm(self):
        pulse_time = self._send_puse_and_wait()
        # To calculate the distance we get the pulse_time and divide it by 2 
        # (the pulse walk the distance twice) and by 29.1 becasue
        # the sound speed on air (343.2 m/s), that It's equivalent to
        # 0.034320 cm/us that is 1cm each 29.1us
        cm = (pulse_time / 2) / 29.1
        return cm

