import requests

def events_by_coin_id():
    ids = ['usdt-tether','btc-bitcoin']
    for coin_id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{coin_id}/events'
        response = requests.get(url)
        response_data = response.json()
        print(response_data)
 
            
events_by_coin_id()