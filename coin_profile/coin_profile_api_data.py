from .models import CoinProfile
from screener.coin_by_id import coin_by_id


def coin_profile_api_data():
    """
    coin_by_id() is imported from screener. it contains data that has taken from dispatching API response,
    Get that data here, format it accordingly and save it to db
    """
    coin_profile_data = coin_by_id()

    coin = CoinProfile()
    coin.coin_id = coin_profile_data["id"]
    coin.name = coin_profile_data["name"]
    coin.symbol = coin_profile_data["symbol"]
    coin.rank = coin_profile_data["rank"]
    coin.is_new = coin_profile_data["is_new"]
    coin.is_active = coin_profile_data["is_active"]
    coin.type = coin_profile_data["type"]
    coin.description = coin_profile_data["description"]
    coin.message = coin_profile_data["message"]
    coin.open_source = coin_profile_data["open_source"]
    coin.started_at = coin_profile_data["started_at"]
    coin.development_status = coin_profile_data["development_status"]
    coin.hardware_wallet = coin_profile_data["hardware_wallet"]
    coin.proof_type = coin_profile_data["proof_type"]
    coin.org_structure = coin_profile_data["org_structure"]
    coin.hash_algorithm = coin_profile_data["hash_algorithm"]
    coin.save()


# coin_profile_api_data()
