import urequests as requests
import network
from time import sleep
# from temp_pico import led1

ssid = 'TP-Link_E08C'
password = '73850007'

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


connect()
url  = "http://192.168.50.178:5001"
r = requests.get(url)
print(r.content)
r.close()