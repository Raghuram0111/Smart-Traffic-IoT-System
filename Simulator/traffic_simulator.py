import requests
import random
import time

SERVER_URL = "http://127.0.0.1:5000/traffic"

locations = ["Junction_A","Junction_B","Junction_C","Junction_D"]

while True:

    data = {
        "location": random.choice(locations),
        "vehicle_count": random.randint(10,120)
    }

    try:
        response = requests.post(SERVER_URL,json=data)
        print("Traffic Data Sent:",data)
    except:
        print("Server not running")

    time.sleep(5)