import os
from .models import Today_OHLC
from coin_profile.models import CoinProfile

from helper import call_api
api_key = os.environ.get('API_KEY')

def today_ohlc_api():
    """
This function fetches today's OHLC data (daily data) for all coins in the 'CoinProfile' model from the FMP API.
The function loops through all the symbols in the 'CoinProfile' model and retrieves their today's OHLC data from 
the Financial Modeling Prep API. The retrieved data is then used to update or create corresponding 'Today_OHLC'
objects in the model.

"""


    symbols = CoinProfile.objects.values_list('symbol', flat=True)
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey=76b77192c1a4d71a0ac45394989d009e"
        response_data = call_api(url)
        if response_data:
            for coin_today_data in response_data:
                symbol = coin_today_data.get("symbol")
                coin_profile = CoinProfile.objects.get(pk=symbol)
                today_ohlc_instance, created = Today_OHLC.objects.update_or_create(
                    symbol=coin_profile,
                    defaults={
                        "open": coin_today_data.get("open"),
                        "previousClose": coin_today_data.get("previousClose"),
                        "day_high": coin_today_data.get("dayHigh"),
                        "day_low": coin_today_data.get("dayLow"),
                        "year_high": coin_today_data.get("yearHigh"),
                        "year_low": coin_today_data.get("yearLow"),
                        "price_avg50": coin_today_data.get("priceAvg50"),
                        "price_avg200": coin_today_data.get("priceAvg200"),
                        "volume": coin_today_data.get("volume"),
                        "avg_volume": coin_today_data.get("avgVolume"),
                        "market_cap": coin_today_data.get("marketCap"),
                        # 'timestamp': coin_today_data.get("timestamp"),
                    }
                )

