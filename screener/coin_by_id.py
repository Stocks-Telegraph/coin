from coin_profile.models import CoinProfile
from helper import call_api

def coin_by_id():
    # ids = ["eth-ethereum"]
    ids = CoinProfile.objects.values_list('symbol', flat=True)[:100]
    coins_data = []
    for symbol in ids:
        print(symbol)
        url = f"https://api.coinpaprika.com/v1/coins/{symbol}"
        response_data = call_api(url)
        if "links" in response_data:
            links = response_data["links"]
            if "explorer" in links:
                explorer_links = links["explorer"]
                iid = response_data.get("id")
                if iid:
                    coins_data.append({"id": iid, "explorer_links": explorer_links})
    return coins_data
                    
# coin_by_id()
