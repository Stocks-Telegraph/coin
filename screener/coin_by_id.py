import requests
from coin_profile.models import CoinProfile

def coin_by_id():
    """
    Retrieve information about a specific cryptocurrency.

    Uses CoinPaprika API to retrieve information about a specific
    cryptocurrency, identified by its `id`.

    Returns:
        dict: A dictionary containing information about the specified cryptocurrency.
    """
    ids = ["eth-ethereum"]
    # ids = CoinProfile.objects.values_list('coin_id', flat=True)
    coins_data = []
    for id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{id}"
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
            coins_data.append(response_data)
        else:
            # print(f"Error retrieving data for coin {id}: {response.text}")
            continue
    return coins_data

coin_by_id()
