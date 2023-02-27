import requests

def events_by_coin_id():
    """
    Retrieve events related to a specific cryptocurrency.

    Uses CoinPaprika API to retrieve events related to a specific
    cryptocurrency, identified by its `id`.

    Returns:
        dict: A dictionary containing events related to the specified cryptocurrency.
    """
    ids = ["btc-bitcoin"]
    for coin_id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/events"
        response = requests.get(url)
        response_data = response.json()
        # print(response_data)


# events_by_coin_id()
