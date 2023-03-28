from .models import CoinProfile
from helper import call_api

def coin_profile_api_data():
    """
This function fetches coin profile data from the Coinpaprika API for all coins in the 'CoinProfile' model. 
It makes use of the helper function 'call_api' to fetch data from the API endpoint.
The function loops through all the coin IDs in the 'CoinProfile' model and retrieves their profile data from 
the Coinpaprika API. The retrieved data is then used to update or create corresponding 'CoinProfile' objects 
in the model. The function prints the symbol of each coin as it processes them.

"""


    ids = CoinProfile.objects.order_by('-coin_id').values_list('coin_id', flat=True)
    for id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{id}"
        coin_data = call_api(url)
        if coin_data is not None:
            symbol = coin_data.get("symbol")
            if symbol is not None:
                print(symbol)
                defaults = {
                    "is_active": coin_data["is_active"],
                    "type": coin_data["type"],
                    "description": coin_data["description"],
                    "started_at": coin_data["started_at"],
                    "proof_type": coin_data["proof_type"],
                    "org_structure": coin_data["org_structure"],
                    "hash_algorithm": coin_data["hash_algorithm"],
                }
                CoinProfile.objects.update_or_create(
                    symbol=symbol+'USD',
                    defaults=defaults,
                )
