from .models import CoinProfile
from screener.coin_by_id import coin_by_id

from helper import call_api


def coin_profile_api_data():

    coins_data = coin_by_id()

    for coin_data in coins_data:
        symbol = coin_data.get("symbol")
        defaults = {
            "is_active": coin_data["is_active"],
            "type": coin_data["type"],
            "description": coin_data["description"],
            "started_at": coin_data["started_at"],
            "proof_type": coin_data["proof_type"],
            "org_structure": coin_data["org_structure"],
            "hash_algorithm": coin_data["hash_algorithm"],
        }
        CoinProfile.objects.update_or_create(
            symbol=symbol,
            defaults=defaults,
        )
