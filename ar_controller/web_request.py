
# import urllib.urequest as requests
from ar_controller.wifi import connect
import json

# import logging

url  = "http://192.168.50.178:5001"
url_f  = "http://192.168.0.100:6001/pico_forward"

url_b  = "http://192.168.0.100:6001/pico_backward"



def trigger_request(dir):
    import urequests as requests

    url  = "http://192.168.50.178:5001"
    url_f  = "http://192.168.0.100:6001/pico_forward"

    url_b  = "http://192.168.0.100:6001/pico_backward"

    # headers = {'content-type': 'application/json'}
    print("trigger request initiated")
    data = {"action":"msg","msg": "wifi"}
    if(dir):
        url = url_f
    else:
        url = url_b
    r = requests.get(url)
    # r = requests.get(url, data= json.dumps(data))

    
    print(r.content)
    r.close()

if __name__ == "__main__":
    wlan = connect()
    trigger_request(dir)