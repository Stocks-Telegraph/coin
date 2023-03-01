from .models import ExplorerLinks
from screener.coin_by_id import coin_by_id


def explorer_links_scripts():
    """
    coin_by_id() is imported from screener. it contains data that has taken from dispatching API response,
    Get that data here, format it accordingly and save it to db
    """

    explorer_links = coin_by_id()
    for explorer_links_data in explorer_links:
        
        if "links" not in explorer_links_data:#Check if there are link for Coin or not
            continue
        links = explorer_links_data["links"]
        
        if "explorer" not in links:
            continue
        links_inside_explorer = links["explorer"]
        

        explosure_link_data_dicionary = {
            "explorer_link_1": links_inside_explorer[0] if len(links_inside_explorer) > 0 else None,#return None if length is smaller than 0.
            "explorer_link_2": links_inside_explorer[1] if len(links_inside_explorer) > 1 else None,
            "explorer_link_3": links_inside_explorer[2] if len(links_inside_explorer) > 2 else None,
            "explorer_link_4": links_inside_explorer[3] if len(links_inside_explorer) > 3 else None,
        }
        print(explosure_link_data_dicionary)
        
    
        explosure_link_instance = ExplorerLinks()
        explosure_link_instance.explorer_link_1 = explosure_link_data_dicionary["explorer_link_1"]
        explosure_link_instance.explorer_link_2 = explosure_link_data_dicionary["explorer_link_2"]
        explosure_link_instance.explorer_link_3 = explosure_link_data_dicionary["explorer_link_3"]
        explosure_link_instance.explorer_link_4 = explosure_link_data_dicionary["explorer_link_4"]
        explosure_link_instance.save()


explorer_links_scripts()
