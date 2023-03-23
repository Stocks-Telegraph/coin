import os
from .models import TickerForSpecificCoin
from coin_profile.models import CoinProfile

from helper import call_api
api_key = os.environ.get('API_KEY')

def ticker_for_a_spec_coin():
    symbols = CoinProfile.objects.values_list('symbol', flat=True)
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
        response_data = call_api(url)
        if response_data:
            for fmp_coin_response in response_data:
                symbol = fmp_coin_response.get('symbol')
                print(symbol)
                coin_profile = CoinProfile.objects.get(symbol=symbol)
                #this part of data is coming from Fmp api
                defaults={
                    'price': fmp_coin_response.get("price"),
                    'change_percentage': fmp_coin_response.get("changesPercentage"),
                    'change': fmp_coin_response.get("change"),
                    'market_cap': fmp_coin_response.get("marketCap"),
                    'year_high': fmp_coin_response.get("yearHigh"),
                    'year_low': fmp_coin_response.get("yearLow")
                }
                TickerForSpecificCoin.objects.update_or_create(
                    symbol=coin_profile,
                    defaults=defaults
                )
