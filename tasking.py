import uasyncio
import machine
from machine import Pin


led1 = Pin('LED', Pin.OUT)
led2 = Pin(18, Pin.OUT)
pin = Pin(18,Pin.IN,Pin.PULL_UP)
interrupt_flag=0

def callback(pin):
    global interrupt_flag
    interrupt_flag=1

pin.irq(trigger=Pin.IRQ_RISING, handler=callback)

async def blink(led, period_ms):
    global interrupt_flag
    while True:
        if(interrupt_flag):
            await uasyncio.sleep_ms(800)
            interrupt_flag = 0
        led.value(1)
        await uasyncio.sleep_ms(5)
        led.value(0)
        await uasyncio.sleep_ms(period_ms)

async def main(led1, led2):
    uasyncio.create_task(blink(led1, 800))
#     uasyncio.create_task(blink(led2, 400))
    await uasyncio.sleep_ms(10_000)

from machine import Pin
uasyncio.run(main(led1, led2))