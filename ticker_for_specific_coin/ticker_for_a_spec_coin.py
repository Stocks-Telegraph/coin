import os
from dateutil.parser import isoparse

from .models import TickerForSpecificCoin
from coin_profile.models import CoinProfile
from screener.fmp_for_a_coin import fmp_for_a_coin
from screener.get_ticker_for_a_specific_coin import get_ticker_for_a_specific_coin

from coin_profile.models import CoinProfile
from helper import call_api
api_key = os.environ.get('API_KEY')

def ticker_for_a_spec_coin():
    # Get ticker data from FMP API
    response_data = fmp_for_a_coin()
    symbols = CoinProfile.objects.values_list('symbol', flat=True)[30:100]
    for symbol in symbols:
        url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={api_key}"
        response_data = call_api(url)
        if response_data:
            for fmp_coin_response in response_data:
                symbol = fmp_coin_response.get('symbol')
                print('Symbol:- ', symbol)
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


    # this part of data is comming from coin-paprika
    # Get ticker data from Coinpaprika API
    coin_data = get_ticker_for_a_specific_coin()
    print('Con_data', coin_data.get('id'))
    # usd_data = coin_data.get("market_data", {}).get("current_price", {}).get("usd", {})

    # specific_coin_instance, created = TickerForSpecificCoin.objects.get_or_create(
    #     symbol=coin_data.get("symbol"),
    #     defaults={
    #         'coin_id': coin_data.get("id"),
    #         'name': coin_data.get("name"),
    #         'circulating_supply': coin_data.get("circulating_supply"),
    #         'total_supply': coin_data.get("total_supply"),
    #         'max_supply': coin_data.get("max_supply"),
    #         'beta_value': coin_data.get("beta_value"),
    #         'first_data_at': isoparse(coin_data.get("first_data_at")),
    #         'last_updated': isoparse(coin_data.get("last_updated")),
    #         'volume_24h': usd_data.get("total_volume"),
    #         'volume_24h_change_24h': usd_data.get("volume_change_percentage_24h"),
    #         'market_cap_change_24h': usd_data.get("market_cap_change_percentage_24h"),
    #         'ath_price': usd_data.get("ath"),
    #         'ath_date': isoparse(coin_data.get("ath_date")),
    #         'percent_from_price_ath': usd_data.get("ath_change_percentage")
    #     }
    # )
