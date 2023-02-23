import requests


def get_today_OHLC():
    ids = ["btc-bitcoin"]
    for coin_id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/ohlcv/today"
        response = requests.get(url)
        response_data = response.json()
        return response_data


get_today_OHLC()
