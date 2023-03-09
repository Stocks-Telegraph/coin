from .models import CoinProfile

from helper import call_api


def coin_profile_api_data():
    # ids = CoinProfile.objects.values_list('coin_id', flat=True)[-10:]
    ids = CoinProfile.objects.order_by('-coin_id').values_list('coin_id', flat=True)[:10]

    for id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{id}"
        coin_data = call_api(url)
        if coin_data is not None:
            symbol = coin_data.get("symbol")
            print(symbol)
            #data not being saved
            if symbol is not None:
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
