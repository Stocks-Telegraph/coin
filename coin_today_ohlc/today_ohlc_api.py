# from screener.get_today_OHLC import get_today_OHLC
from .models import Today_OHLC
from screener.fmp_for_a_coin import fmp_for_a_coin
from coin_profile.models import CoinProfile


def today_ohlc_api():
    """Get Any Crytpo's Today Data"""
    response_data = fmp_for_a_coin()
    print(response_data)
    if response_data:
        for coin_data in response_data:
            for coin_today_data in coin_data:
                

                # Get the CoinProfile instance for the symbol
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
