from machine import Pin

interrupt_flag=0
# pin = Pin(18,Pin.IN,Pin.PULL_UP)
pin = Pin(20,Pin.IN,Pin.PULL_UP)

def callback(pin):
    global interrupt_flag
    interrupt_flag=1

pin.irq(trigger=Pin.IRQ_RISING, handler=callback)
while True:
    if interrupt_flag is 1:
        print("Interrupt has occured")
        interrupt_flag=0