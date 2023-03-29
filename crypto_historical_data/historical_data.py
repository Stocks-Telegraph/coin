import os
from coin_profile.models import CoinProfile
from datetime import datetime, timedelta
from .models import CryptoHistoricalData
from helper import call_api

api_key = os.environ.get("API_KEY")

def historical_data():

    '''Run the Script , and it will save 2 years of data for each and every symbols.'''
    symbols = CoinProfile.objects.values_list('symbol', flat=True)[:50]
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={api_key}"
        response_data = call_api(url)
        if response_data is not None and "historical" in response_data:
            for crypto_data in response_data["historical"]:
                date_str = crypto_data["date"]
                date = datetime.strptime(date_str, "%Y-%m-%d")
                two_years_ago = datetime.now() - timedelta(days=365*2)
                if date >= two_years_ago:
                    symbol_instance = CoinProfile.objects.get(symbol=response_data["symbol"])
                    data = {
                        "date": crypto_data["date"],
                        "open": crypto_data["open"],
                        "high": crypto_data["high"],
                        "low": crypto_data["low"],
                        "close": crypto_data["close"],
                        "volume": crypto_data["volume"],
                    }
                    crypto_data_instance, created = CryptoHistoricalData.objects.update_or_create(
                        symbol=symbol_instance,
                        date=date_str,
                        defaults=data
                    )

