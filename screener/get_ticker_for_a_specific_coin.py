import requests


def get_ticker_for_a_specific_coin():
    """
    Retrieve the ticker information for a specific cryptocurrency.

    Uses CoinPaprika API to retrieve the ticker information for aspecific cryptocurrency,
    identified by its `id`. The ticker information includes
    data such as the current price, volume, and market cap of the cryptocurrency.
    """
    ids = ["btc-bitcoin"]
    for coin_id in ids:
        url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
        response = requests.get(url)
        response_data = response.json()
        return response_data


get_ticker_for_a_specific_coin()
