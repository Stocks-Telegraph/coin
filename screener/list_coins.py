import requests

def list_coins():
    url = "https://api.coinpaprika.com/v1/coins"
    response = requests.get(url)
    response_data = response.json()
    # for coin_data in response_data:
    # return coin_data


# list_coins()
