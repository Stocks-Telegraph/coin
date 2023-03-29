from coin_profile.models import CoinProfile
from .models import ExplorerLinks

from .api_scripts.coinpaprika_explorer_links import coinpaprika_explorer_links

def explorer_links_scripts():
    """
This function fetches the social media links for coins using the 'coinpaprika_explorer_links' 
function from the 'api_scripts' module. It then updates or creates social media links for each coin 
in the 'CoinProfile' model by creating or updating a corresponding 'ExplorerLinks' object. 

"""
    coins_explorer_links = coinpaprika_explorer_links()
    for coin_data in coins_explorer_links:
        print(coin_data)
        coin_name = coin_data["id"]
        try:
            all_explorer_links = coin_data["explorer_links"]
            print('Message:', all_explorer_links)
            coin_profile = CoinProfile.objects.get(coin_id=coin_name)
            for explorer_link in all_explorer_links:
                ExplorerLinks.objects.update_or_create(
                    symbol=coin_profile,
                    explorer_link=explorer_link,
                )
            # all_explorer_links = coin_data["explorer_links"]
            # explorure_link_dicionary = {
            #     "explorer_link_1": all_explorer_links[0] if len(all_explorer_links) > 0 else None,
            #     "explorer_link_2": all_explorer_links[1] if len(all_explorer_links) > 1 else None,
            #     "explorer_link_3": all_explorer_links[2] if len(all_explorer_links) > 2 else None,
            #     "explorer_link_4": all_explorer_links[3] if len(all_explorer_links) > 3 else None,
            # }
            # coin_profile = CoinProfile.objects.get(coin_id=coin_name)
            # ExplorerLinks.objects.update_or_create(
            #     symbol=coin_profile,
            #     defaults=explorure_link_dicionary,
            # )
        except:
            pass

# explorer_links_scripts()
