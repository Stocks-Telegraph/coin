from .fmp_coin import fmp_api_coin
import re
from coin_profile.models import CoinProfile


def fmp_all_coins():
    response_data = fmp_api_coin()
    all_coins = []
    
    for coin in response_data:
        symbol = coin.get('symbol')
        name = coin.get('name')

        # Use regular expressions to remove "USD" from symbol and name
        symbol = re.sub(r"USD", "", symbol)
        name = re.sub(r"USD", "", name)

        name = re.sub(r"\.", "", name)

        coin_ids = f"{symbol.lower()}-{name.lower().replace(' ', '-')}"
        if coin_ids.endswith("-"):
            coin_ids = coin_ids[:-1] + ""
            all_coins.append(coin_ids)

            coin_profile = CoinProfile()
            coin_profile.symbol = symbol
            coin_profile.name = name
            coin_profile.coin_id = coin_ids
            coin_profile.save()
    return all_coins