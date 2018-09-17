import json
import time
import requests
import psutil


while True:
    data = {
        "app": "pinger",
        "sensor": "cpu",
        "value": psutil.cpu_percent()
    }
    requests.post("http://statuschecker:8000/status/", json.dumps(data))
    time.sleep(10)
