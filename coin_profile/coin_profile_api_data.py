from .models import CoinProfile
from screener.coin_by_id import coin_by_id


def coin_profile_api_data():
    """
    Retrieves data for a set of cryptocurrencies, formats it, and saves it to the database.
    """
    coins_data = coin_by_id()

    for coin_data in coins_data:
        symbol = coin_data.get("symbol")
        coin_profile = CoinProfile.objects.get(pk=symbol)

        coin_profile.is_active = coin_data["is_active"]
        coin_profile.type = coin_data["type"]
        coin_profile.description = coin_data["description"]
        coin_profile.started_at = coin_data["started_at"]
        coin_profile.proof_type = coin_data["proof_type"]
        coin_profile.org_structure = coin_data["org_structure"]
        coin_profile.hash_algorithm = coin_data["hash_algorithm"]
        coin_profile.save()
