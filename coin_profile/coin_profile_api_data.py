from .models import CoinProfile
from screener.coin_by_id import coin_by_id


def coin_profile_api_data():
    """
    Retrieves data for a set of cryptocurrencies, formats it, and saves it to the database.
    """
    coins_data = coin_by_id()

    for coin_data in coins_data:
        coin = CoinProfile()
        coin.coin_id = coin_data["id"]
        coin.name = coin_data["name"]
        coin.symbol = coin_data["symbol"]
        coin.rank = coin_data["rank"]
        coin.is_new = coin_data["is_new"]
        coin.is_active = coin_data["is_active"]
        coin.type = coin_data["type"]
        coin.description = coin_data["description"]
        coin.message = coin_data["message"]
        coin.open_source = coin_data["open_source"]
        coin.started_at = coin_data["started_at"]
        coin.development_status = coin_data["development_status"]
        coin.hardware_wallet = coin_data["hardware_wallet"]
        coin.proof_type = coin_data["proof_type"]
        coin.org_structure = coin_data["org_structure"]
        coin.hash_algorithm = coin_data["hash_algorithm"]

        try:
            coin.save()
        except Exception as e:
            print(f"Error saving {coin.name}: {str(e)}")
