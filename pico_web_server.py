import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
from machine import Pin

led = Pin('LED', Pin.OUT)

ssid = 'TP-Link_E08C'
password = '73850007'


def web_server(wlan):
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )

    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)


    s.listen(1)

    print('listening on', addr)

    # Listen for connections
    while True:
        try:
            cl, addr = s.accept()
            print('client connected from', addr)
            request = cl.recv(1024)
            print(request)

            request = str(request)
            led_on = request.find('/light/on')
            led_off = request.find('/light/off')
            print( 'led on = ' + str(led_on))
            print( 'led off = ' + str(led_off))

            if led_on >0 :
                print("led on")
                led.value(1)
                stateis = "LED is ON"

            if led_off >0:
                print("led off")
                led.value(0)
                stateis = "LED is OFF"

            # response = html % stateis

            cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
            # cl.send(response)
            cl.close()

        except OSError as e:
            cl.close()
            print('connection closed')

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)

    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
    return wlan


try:
    wlan = connect()
    web_server(wlan)
except KeyboardInterrupt:
    machine.reset()