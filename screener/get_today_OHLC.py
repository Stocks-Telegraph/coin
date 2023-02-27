import requests


def get_today_OHLC():
    """
    Retrieve today's data for a specific cryptocurrency.

    Uses CoinPaprika API to retrieve today's data such as Open, High, Low, and Close prices
    for a specific cryptocurrency,identified by its `id`.
 
    Returns:
        dict: A dictionary containing the OHLC price data for the specified cryptocurrency.
    """
    ids = ["btc-bitcoin"]
    for coin_id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/ohlcv/today"
        response = requests.get(url)
        response_data = response.json()
        return response_data


get_today_OHLC()
