from coin_profile.models import CoinProfile

from helper import call_api

def coinpaprika_social_links():

    """
This function retrieves Social links for all the coins present in the CoinProfile model from the Coinpaprika API. 
It makes use of the helper function 'call_api' to fetch data from the API endpoint. 
The function loops through all the coin IDs in the CoinProfile model and
checks if they have social links(fb,github,youtube,website etc) available in their API response data. 
"""

    ids = CoinProfile.objects.values_list('coin_id', flat=True)[3300:]

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
