import requests
from coin_profile.models import CoinProfile

def list_coins():
    """
    Fetches the list of all coins available on CoinPaprika API.

    Returns:
        A list of dictionaries containing coin data like id, name, symbol, etc.
    """
    url = "https://api.coinpaprika.com/v1/coins"
    response = requests.get(url)
    response_data = response.json()
    return response_data
    # for coin_data in response_data:
    #     # print(coin_data)
    #     coin_data_instance = CoinProfile()
    #     coin_data_instance.coin_id = coin_data["id"]
    #     coin_data_instance.name = coin_data["name"]
    #     coin_data_instance.symbol = coin_data["symbol"]
    #     coin_data_instance.rank = coin_data["rank"]
    #     coin_data_instance.is_new = coin_data["is_new"]
    #     coin_data_instance.is_active = coin_data["is_active"]
    #     coin_data_instance.type = coin_data["type"]
    #     try:
    #         coin_data_instance.save()
    #     except Exception as e:
    #         print(f"Error saving {coin_data_instance.coin_id}: {str(e)}")


list_coins()
