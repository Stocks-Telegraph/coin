import requests
import pandas as pd


def coin_by_id():
    ids = ['btc-bitcoin']
    for id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{id}'
        response = requests.get(url)
        response_data = response.json()
        for explorer_link in response_data['links']['explorer']:
            data = {
                "id": response_data["id"],
                "name": response_data["name"],
                "symbol": response_data["symbol"],
                "rank": response_data["rank"],
                "is_new": response_data["is_new"],
                "is_active": response_data["is_active"],
                "type": response_data["type"],
                "description": response_data["description"],
                "message": response_data["message"],
                "open_source": response_data["open_source"],
                "started_at": response_data["started_at"],
                "development_status": response_data["development_status"],
                "hardware_wallet": response_data["hardware_wallet"],
                "proof_type": response_data["proof_type"],
                "org_structure": response_data["org_structure"],
                "hash_algorithm": response_data["hash_algorithm"],
                'explorer_link_1' : response_data['links']['explorer'][0],
                'explorer_link_2' : response_data['links']['explorer'][1],
                'explorer_link_3' : response_data['links']['explorer'][2],
                'explorer_link_4' : response_data['links']['explorer'][3],
                'facebook': response_data['links']['facebook'],
                'reddit': response_data['links']['reddit'],
                'source_code':response_data['links']['source_code'],
                'website':response_data['links']['website'],
                'youtube_link ':response_data['links']['youtube'][0],
            }
        

coin_by_id()