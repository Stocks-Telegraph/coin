import requests
from coin_profile.models import CoinProfile

def coin_by_id():
    ids = ['btc-bitcoin','eth-ethereum','bnb-binance-coin','ada-cardano']
    for id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{id}'
        response = requests.get(url)
        response_data = response.json()
          
        coin = CoinProfile()
        coin.coin_id = response_data["id"]
        coin.name = response_data["name"]
        coin.symbol = response_data["symbol"]
        coin.rank = response_data["rank"]
        coin.is_new = response_data["is_new"]
        coin.is_active = response_data["is_active"]
        coin.type = response_data["type"]
        coin.description = response_data["description"]
        coin.message = response_data["message"]
        coin.open_source = response_data["open_source"]
        coin.started_at = response_data["started_at"]
        coin.development_status =  response_data["development_status"]
        coin.hardware_wallet =  response_data["hardware_wallet"]
        coin.proof_type = response_data["proof_type"]
        coin.org_structure = response_data["org_structure"]
        coin.hash_algorithm = response_data["hash_algorithm"]
        coin.save()

# coin_by_id()