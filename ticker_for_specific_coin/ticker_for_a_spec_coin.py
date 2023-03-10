import os
from dateutil.parser import isoparse

from .models import TickerForSpecificCoin
from coin_profile.models import CoinProfile

from coin_profile.models import CoinProfile
from helper import call_api
api_key = os.environ.get('API_KEY')

def ticker_for_a_spec_coin():
    symbols = CoinProfile.objects.values_list('symbol', flat=True)[70:100]
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
        response_data = call_api(url)
        if response_data:
            for fmp_coin_response in response_data:
                symbol = fmp_coin_response.get('symbol')
                coin_profile = CoinProfile.objects.get(symbol=symbol)
                #this part of data is coming from Fmp api
                specific_coin_instance, created = TickerForSpecificCoin.objects.get_or_create(
                    symbol=coin_profile,
                    defaults={
                        'price': fmp_coin_response.get("price"),
                        'change_percentage': fmp_coin_response.get("changesPercentage"),
                        'market_cap': fmp_coin_response.get("marketCap"),
                        'year_high': fmp_coin_response.get("yearHigh"),
                        'year_low': fmp_coin_response.get("yearLow")
                    }
                )


#post below from postman
"""
{
    "symbol": "BTC",
    "circulating_supply": 18500000,
    "total_supply": 21000000,
    "max_supply": 21000000,
    "beta_value": 0.5,
    "first_data_at": "2021-01-01T00:00:00Z",
    "last_updated": "2021-03-10T10:00:00Z",
    "price": 50000,
    "volume_24h": 50000000000,
    "volume_24h_change_24h": 1.2,
    "market_cap": 925000000000,
    "market_cap_change_24h": 0.8,
    "change_percentage": 1.5,
    "year_high": 65000,
    "year_low": 30000
}
make sure to change symbol"""