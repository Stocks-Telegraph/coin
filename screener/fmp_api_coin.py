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
        if name:
            name = re.sub(r"USD", "", name)
            name = re.sub(r"\.", "", name)
        else:
            name=""
        coin_ids = f"{symbol.lower()}-{name.lower().replace(' ', '-')}"
        if coin_ids.endswith("-"):
            coin_ids = coin_ids[:-1] + ""

        if CoinProfile.objects.filter(symbol=symbol + 'USD').exists():
            continue

        coin_profile, created = CoinProfile.objects.update_or_create(
            coin_id=coin_ids,
            defaults={
                'symbol': symbol + 'USD',
                'name': name
            }
        )

        if created:
            all_coins.append(coin_ids)

    return all_coins
