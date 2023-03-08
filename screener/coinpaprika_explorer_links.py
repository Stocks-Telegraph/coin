import requests
from coin_profile.models import CoinProfile

from helper import call_api

def coinpaprika_explorer_links():
    # ids = ["eth-ethereum"]
    ids = CoinProfile.objects.values_list('coin_id', flat=True)[40:60]
    coins_data = []
    for id in ids:
        print(id)
        url = f"https://api.coinpaprika.com/v1/coins/{id}"
        response_data = call_api(url)
        print(response_data)
        if "links" in response_data:
            links = response_data["links"]
            if "explorer" in links:
                explorer_links = links["explorer"]
                iid = response_data.get("id")
                if iid:
                    coins_data.append({"id": iid, "explorer_links": explorer_links})
    return coins_data

