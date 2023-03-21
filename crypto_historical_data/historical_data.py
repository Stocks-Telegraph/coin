import os
from coin_profile.models import CoinProfile

from helper import call_api

api_key = os.environ.get("API_KEY")


def historical_data():
    # symbols = CoinProfile.objects.values_list('symbol', flat=True)
    symbols = ["BTCUSD"]
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={api_key}"
        response_data = call_api(url)
        print(response_data["symbol"])
        for crypto_data in response_data["historical"]:
            symbol_data = {
                "symbol": response_data["symbol"],
                "date": crypto_data["date"],
                "open": crypto_data["open"],
                "high": crypto_data["high"],
                "low": crypto_data["low"],
                "close": crypto_data["close"],
                "adjClose": crypto_data["adjClose"],
                "volume": crypto_data["volume"],
                "unadjustedVolume": crypto_data["unadjustedVolume"],
                "change": crypto_data["change"],
                "changePercent": crypto_data["changePercent"],
                "vwap": crypto_data["vwap"],
                "changeOverTime": crypto_data["changeOverTime"],
            }
            print(symbol_data)
