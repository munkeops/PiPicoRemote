from machine import Pin
import time

from ar_controller.web_request import trigger_request
from ar_controller.wifi import connect

wlan = connect()


interrupt_flag_f=0
interrupt_flag_b=0

debounce_time=0

pin_f = Pin(18,Pin.IN,Pin.PULL_UP)
pin_b = Pin(20,Pin.IN,Pin.PULL_UP)

def callback_f(pin):
    global interrupt_flag_f, debounce_time
    if (time.ticks_ms()-debounce_time) > 500:
        interrupt_flag_f= 1
        debounce_time=time.ticks_ms()

def callback_b(pin):
    global interrupt_flag_b, debounce_time
    if (time.ticks_ms()-debounce_time) > 500:
        interrupt_flag_b= 1
        debounce_time=time.ticks_ms()

pin_f.irq(trigger=Pin.IRQ_FALLING, handler=callback_f)

pin_b.irq(trigger=Pin.IRQ_FALLING, handler=callback_b)


print("started")
while True:
    if interrupt_flag_f is 1:
        print("Forward button pressed")
        trigger_request(1)
        interrupt_flag_f=0
    if interrupt_flag_b is 1:
        print("Backward button pressed")
        trigger_request(0)
        interrupt_flag_b=0
    