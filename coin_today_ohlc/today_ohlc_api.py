from screener.get_today_OHLC import get_today_OHLC
from .models import Today_OHLC

def today_ohlc_api():
   today_ohlc_api_response_data = get_today_OHLC()
   
   for today_ohlc_api_data in today_ohlc_api_response_data:
       today_ohlc_instance = Today_OHLC()
       
       today_ohlc_instance.time_open = today_ohlc_api_data["time_open"]
       today_ohlc_instance.time_close = today_ohlc_api_data["time_close"]
       today_ohlc_instance.open = today_ohlc_api_data["open"]
       today_ohlc_instance.high = today_ohlc_api_data["high"]
       today_ohlc_instance.low = today_ohlc_api_data["low"]
       today_ohlc_instance.close = today_ohlc_api_data["close"]
       today_ohlc_instance.volume = today_ohlc_api_data["volume"]
       today_ohlc_instance.market_cap = today_ohlc_api_data["market_cap"]
       today_ohlc_instance.save()
       break