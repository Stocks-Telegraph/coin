import os
from .models import Today_OHLC
from coin_profile.models import CoinProfile

from helper import call_api
api_key = os.environ.get('API_KEY')

def today_ohlc_api():
    symbols = CoinProfile.objects.values_list('symbol', flat=True)
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
        response_data = call_api(url)
        if response_data:
            for coin_today_data in response_data:
                symbol = coin_today_data.get("symbol")
                coin_profile = CoinProfile.objects.get(pk=symbol)
                today_ohlc_instance, created = Today_OHLC.objects.update_or_create(
                    symbol=coin_profile,
                    defaults={
                        "time_open": coin_today_data.get("open"),
                        "time_close": coin_today_data.get("previousClose"),
                        "high": coin_today_data.get("dayHigh"),
                        "low": coin_today_data.get("dayLow"),
                        "volume": coin_today_data.get("volume"),
                        "market_cap": coin_today_data.get("marketCap"),
                    }
                )
                    
                # today_ohlc_instance.time_open = coin_today_data.get("open")
                # today_ohlc_instance.time_close = coin_today_data.get("previousClose")
                # today_ohlc_instance.open = today_ohlc_api_data["open"]
                # today_ohlc_instance.close = today_ohlc_api_data["close"]

# today_ohlc_api()
