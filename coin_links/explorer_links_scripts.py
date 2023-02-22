import requests
from .models import ExplosureLinks

def explorer_links_scripts():
    ids = ['btc-bitcoin','eth-ethereum','busd-binance-usd','ada-cardano']
    for id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{id}'
        response = requests.get(url)
        response_data = response.json()
        links = response_data['links']
        explorerlinks = links['explorer']
        
        explosure_link_data = {
                'explorer_link_1' : explorerlinks[0] if len(explorerlinks) > 0 else None,
                'explorer_link_2' : explorerlinks[1] if len(explorerlinks) > 1 else None,
                'explorer_link_3' : explorerlinks[2] if len(explorerlinks) > 2 else None,
                'explorer_link_4' : explorerlinks[3] if len(explorerlinks) > 3 else None,
                }
            
        explosure_link_instance = ExplosureLinks()
        explosure_link_instance.explorer_link_1 = explosure_link_data['explorer_link_1']
        explosure_link_instance.explorer_link_2 = explosure_link_data['explorer_link_2']
        explosure_link_instance.explorer_link_3 = explosure_link_data['explorer_link_3']
        explosure_link_instance.explorer_link_4 = explosure_link_data['explorer_link_4']
        explosure_link_instance.save()  

# explorer_links_scripts()