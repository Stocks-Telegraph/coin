import requests
import pandas as pd


def coin_by_id():
    ids = ["btc-bitcoin"]
    for id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{id}"
        response = requests.get(url)
        response_data = response.json()
        return response_data


coin_by_id()
