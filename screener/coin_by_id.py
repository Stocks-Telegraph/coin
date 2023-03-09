from coin_profile.models import CoinProfile
from helper import call_api

def coin_by_id():
    # ids = ["eth-ethereum"]
    ids = CoinProfile.objects.values_list('coin_id', flat=True)[:100]
    coins_data = []
    for id in ids:
        print(id)
        url = f"https://api.coinpaprika.com/v1/coins/{id}"
        response_data = call_api(url)
        print(response_data)
                    
# coin_by_id()
