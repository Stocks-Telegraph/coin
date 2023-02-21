import requests
import pandas as pd


def events_by_coin_id():
    ids = ['usdt-tether','btc-bitcoin']
    for coin_id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{coin_id}/events'
        response = requests.get(url)
        response_data = response.json()

        # for event_by_coin_response in response_data:
        #     return event_by_coin_response
            

            
events_by_coin_id()