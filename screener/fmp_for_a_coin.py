import os
from coin_profile.models import CoinProfile
from helper import call_api
api_key = os.environ.get('API_KEY')

def fmp_for_a_coin():
    symbols = CoinProfile.objects.values_list('symbol', flat=True)[30:40]
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
        response_data = call_api(url)
    return response_data
    
