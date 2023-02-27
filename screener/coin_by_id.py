import requests

def coin_by_id():
    """
    Retrieve information about a specific cryptocurrency.

    Uses CoinPaprika API to retrieve information about a specific
    cryptocurrency, identified by its `id`.

    Returns:
        dict: A dictionary containing information about the specified cryptocurrency.
    """
    ids = ["btc-bitcoin"]
    for id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{id}"
        response = requests.get(url)
        response_data = response.json()
        return response_data


coin_by_id()
