#from machine import Pin
#onboardLED = Pin('LED', Pin.OUT)
#onboardLED.value(1)

from machine import Pin
import time

led2 = Pin(18, Pin.OUT)
led3 = Pin(19, Pin.OUT)
led4 = Pin(20, Pin.OUT)

led1 = Pin('LED', Pin.OUT)

while(1):
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)

    

    print("making value high and sleeping")
    time.sleep(2)
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    time.sleep(2)

