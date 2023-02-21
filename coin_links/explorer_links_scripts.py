import requests
import pandas as pd
from .models import ExplosureLinks

def explorer_links_scripts():
    ids = ['eth-ethereum','usdt-tether']
    for id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{id}'
        response = requests.get(url)
        response_data = response.json()
        links = response_data['links']
        explorerlinks = links['explorer']
        data = {
                'explorer_link_1' : explorerlinks[0],
                'explorer_link_2' : explorerlinks[1],
                'explorer_link_3' : explorerlinks[2],
                'explorer_link_4' : explorerlinks[3],
            }
            
        explosure_link_instance = ExplosureLinks()
        explosure_link_instance.explorer_link_1 = data['explorer_link_1']
        explosure_link_instance.explorer_link_2 = data['explorer_link_2']
        explosure_link_instance.explorer_link_3 = data['explorer_link_3']
        explosure_link_instance.explorer_link_4 = data['explorer_link_4']
        explosure_link_instance.save()
        break
        

explorer_links_scripts()