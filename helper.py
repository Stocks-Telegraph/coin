import requests

def call_api(URL, return_value=None):
    print(URL)
    response = requests.get(URL)
    print(response)
    if response.status_code == 200:
        return response.json()
    return return_value