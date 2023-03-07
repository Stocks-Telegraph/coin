import requests
import os

from coin_profile.models import CoinProfile

api_key = os.environ.get('API_KEY')

def fmp_for_a_coin():
    # symbols = CoinProfile.objects.values_list('symbol', flat=True)
    symbols = ['ETH']
    coins_data = []
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
            coins_data.append(response_data)
            # return response_data
    return coins_data

fmp_for_a_coin()