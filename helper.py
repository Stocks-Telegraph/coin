import requests
import time
import random


def call_api(URL, return_value=None):
    print(URL)
    response = requests.get(URL)
    print(response)
    time.sleep(random.randrange(8,11))
    if response.status_code == 200:
        return response.json()
    return return_value