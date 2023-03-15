import os
from dateutil.parser import isoparse

from .models import TickerForSpecificCoin
from coin_profile.models import CoinProfile
from coin_profile.models import CoinProfile

from helper import call_api
api_key = os.environ.get('API_KEY')

def cp_ticker_for_spec_coin():
    ids = CoinProfile.objects.values_list('coin_id', flat=True)
    for coin_id in ids:
        url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
        response_data = call_api(url)
        if response_data is not None:
            usd_data = response_data.get("market_data", {}).get("current_price", {}).get("usd", {})
            defaults={
                'circulating_supply': response_data.get("circulating_supply"),
                'total_supply': response_data.get("total_supply"),
                'max_supply': response_data.get("max_supply"),
                'beta_value': response_data.get("beta_value"),
                'first_data_at': isoparse(response_data.get("first_data_at")),
                'last_updated': isoparse(response_data.get("last_updated")),
                'volume_24h': usd_data.get("total_volume"),
                'volume_24h_change_24h': usd_data.get("volume_change_percentage_24h"),
                'market_cap_change_24h': usd_data.get("market_cap_change_percentage_24h"),
            }
            coin_profile = CoinProfile.objects.get(coin_id=coin_id)
            specific_coin_instance, created = TickerForSpecificCoin.objects.update_or_create(
                symbol=coin_profile,
                defaults=defaults,
            )

        else:
            pass