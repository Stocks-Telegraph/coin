from coin_profile.models import CoinProfile

from helper import call_api

def coinpaprika_social_links():
    ids = CoinProfile.objects.values_list('coin_id', flat=True)[:20]
    coins_data = []
    for id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{id}"
        response_data = call_api(url)
        try:
            if "links" in response_data:
                links = response_data["links"]
                iid = response_data.get("id")
                if iid:
                    coins_data.append({"id": iid, "Social_links": links})
        except:
            continue
    return coins_data
