import network
from time import sleep
# from temp_pico import led1

ssid = 'TP-Link_E08C'
password = '73850007'

# ssid = 'PlansForDinner?'
# password = 'Nageswararao'

def connect():
    #Connect to WLAN

    print(ssid)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)

    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    
    return wlan
