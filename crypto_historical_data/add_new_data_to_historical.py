import os
from datetime import datetime
from .models import CryptoHistoricalData
from coin_profile.models import CoinProfile
from helper import call_api

api_key = os.environ.get("API_KEY")

def add_new_data_to_historical():
    '''Before running this script, make sure that the data for all the symbols or a specific 
    symbol is saved in database.
    This script will add new (today) data to database and will remove the very last data .'''
     # symbols = CoinProfile.objects.values_list('symbol', flat=True)
    symbols = ["BTCUSD"]
    today = datetime.today().strftime('%Y-%m-%d')
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={api_key}"
        response_data = call_api(url)
        historical_response_data = response_data["historical"]
        historical_data = [data for data in historical_response_data if data["date"] == today]
        
        symbol_instance = CoinProfile.objects.get(symbol=response_data["symbol"])
        for today_data in historical_data:
            if today_data:
            # Create a new CryptoHistoricalData object using today's data
                CryptoHistoricalData.objects.update_or_create(
                symbol=symbol_instance,
                date=datetime.strptime(today, '%Y-%m-%d').date(),
                defaults={
                    'open': today_data["open"],
                    'high': today_data["high"],
                    'low': today_data["low"],
                    'close': today_data["close"],
                    'volume': today_data["volume"]
                }
            )

        oldest_data = CryptoHistoricalData.objects.filter(symbol=symbol).order_by('date').first()
        # print(oldest_data)
        if oldest_data:
            oldest_data.delete()
        
       
