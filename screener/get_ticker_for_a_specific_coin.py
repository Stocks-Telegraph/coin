import requests


def get_ticker_for_a_specific_coin():
    ids = ["btc-bitcoin"]
    for coin_id in ids:
        url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
        response = requests.get(url)
        response_data = response.json()
        return response_data


get_ticker_for_a_specific_coin()
