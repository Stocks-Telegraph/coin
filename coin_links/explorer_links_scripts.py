from .models import ExplorerLinks
from coin_profile.models import CoinProfile

from screener.coin_by_id import coin_by_id


def explorer_links_scripts():
    """
    coin_by_id() is imported from screener. it contains data that has taken from dispatching API response,
    Get that data here, format it accordingly and save it to db
    """

    explorer_links = coin_by_id()
    if not explorer_links:
        pass

    for explorer_links_data in explorer_links:
        if ("links" not in explorer_links_data):  # Check if there are links for Coin or not
            continue
        links = explorer_links_data["links"]

        if "explorer" not in links:
            continue
        links_inside_explorer = links["explorer"]

        explosure_link_data_dicionary = {
            "explorer_link_1": links_inside_explorer[0]
            if len(links_inside_explorer) > 0
            else None,  # return None if length is smaller than 0.
            "explorer_link_2": links_inside_explorer[1]
            if len(links_inside_explorer) > 1
            else None,
            "explorer_link_3": links_inside_explorer[2]
            if len(links_inside_explorer) > 2
            else None,
            "explorer_link_4": links_inside_explorer[3]
            if len(links_inside_explorer) > 3
            else None,
        }
        # Get the relative coin id
        symbol = explorer_links_data.get("symbol")
        coin_profile = CoinProfile.objects.get(pk=symbol)

        explosure_link_instance, created = ExplorerLinks.objects.get_or_create(
            symbol=coin_profile
        )
        explosure_link_instance.explorer_link_1 = explosure_link_data_dicionary[
            "explorer_link_1"
        ]
        explosure_link_instance.explorer_link_2 = explosure_link_data_dicionary[
            "explorer_link_2"
        ]
        explosure_link_instance.explorer_link_3 = explosure_link_data_dicionary[
            "explorer_link_3"
        ]
        explosure_link_instance.explorer_link_4 = explosure_link_data_dicionary[
            "explorer_link_4"
        ]
        explosure_link_instance.save()


explorer_links_scripts()
