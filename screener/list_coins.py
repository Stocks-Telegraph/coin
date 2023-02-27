import requests


def list_coins():
    """
    Fetches the list of all coins available on CoinPaprika API.

    Returns:
        A list of dictionaries containing coin data like id, name, symbol, etc.
    """
    url = "https://api.coinpaprika.com/v1/coins"
    response = requests.get(url)
    response_data = response.json()
    # for coin_data in response_data:
    # return coin_data


# list_coins()
