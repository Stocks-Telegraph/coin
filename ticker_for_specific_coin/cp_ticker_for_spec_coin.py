import os
from dateutil.parser import isoparse

from .models import TickerForSpecificCoin
from coin_profile.models import CoinProfile
# from screener.fmp_for_a_coin import fmp_for_a_coin
# from screener.get_ticker_for_a_specific_coin import get_ticker_for_a_specific_coin

from coin_profile.models import CoinProfile
from helper import call_api
api_key = os.environ.get('API_KEY')

def cp_ticker_for_spec_coin():
    ids = CoinProfile.objects.values_list('coin_id', flat=True)[30:100]
    for coin_id in ids:
        coin_profile = CoinProfile.objects.get(coin_id=coin_id)
        url = f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
        response_data = call_api(url)
        print(response_data)
        if response_data is not None:
            # for fmp_coin_response in response_data:
            usd_data = response_data.get("market_data", {}).get("current_price", {}).get("usd", {})

            specific_coin_instance, created = TickerForSpecificCoin.objects.get_or_create(
            symbol=coin_profile,
            defaults={
                # 'coin_id': response_data.get("id"),
                # 'name': response_data.get("name"),
                'circulating_supply': response_data.get("circulating_supply"),
                'total_supply': response_data.get("total_supply"),
                'max_supply': response_data.get("max_supply"),
                'beta_value': response_data.get("beta_value"),
                'first_data_at': isoparse(response_data.get("first_data_at")),
                'last_updated': isoparse(response_data.get("last_updated")),
                'volume_24h': usd_data.get("total_volume"),
                'volume_24h_change_24h': usd_data.get("volume_change_percentage_24h"),
                'market_cap_change_24h': usd_data.get("market_cap_change_percentage_24h"),
                # 'ath_price': usd_data.get("ath"),
                # 'ath_date': isoparse(response_data.get("ath_date")),
                # 'percent_from_price_ath': usd_data.get("ath_change_percentage")
            }
        )
 
        else:
            print('Error')