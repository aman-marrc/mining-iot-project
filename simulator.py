import requests
import time
import random

URL = "http://127.0.0.1:5000/data"

lat = 23.8
lon = 86.4

while True:
    lat += random.uniform(-0.001, 0.001)
    lon += random.uniform(-0.001, 0.001)
    speed = random.choice([0, 20, 30])

    data = {
        "lat": lat,
        "lon": lon,
        "speed": speed,
        "timestamp": time.time()
    }

    res = requests.post(URL, json=data)
    print(data, res.json())

    time.sleep(2)