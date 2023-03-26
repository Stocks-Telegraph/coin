import requests

def call_api(URL, return_value=None):
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    return return_value