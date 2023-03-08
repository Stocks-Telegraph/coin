import re
from coin_profile.models import CoinProfile
from helper import call_api

def fmp_all_coins():
    url = "https://financialmodelingprep.com/api/v3/quotes/crypto?apikey=76b77192c1a4d71a0ac45394989d009e"
    response_data = call_api(url)
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