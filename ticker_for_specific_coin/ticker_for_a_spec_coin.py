from dateutil.parser import isoparse

from .models import TickerForSpecificCoin
from coin_profile.models import CoinProfile
from screener.fmp_for_a_coin import fmp_for_a_coin
from screener.get_ticker_for_a_specific_coin import get_ticker_for_a_specific_coin


def ticker_for_a_spec_coin():
    # Get ticker data from FMP API
    response_data = fmp_for_a_coin()
    if response_data:
        for fmp_response in response_data:
            for crypto_data_fmp in fmp_response:
                symbol = crypto_data_fmp.get('symbol')
                coin_profile = CoinProfile.objects.get(symbol=symbol)
                
                #this part of data is coming from Fmp api
                specific_coin_instance, created = TickerForSpecificCoin.objects.get_or_create(
                    symbol=coin_profile,
                    defaults={
                        'price': crypto_data_fmp.get("price"),
                        'change_percentage': crypto_data_fmp.get("changesPercentage"),
                        'market_cap': crypto_data_fmp.get("marketCap"),
                        'year_high': crypto_data_fmp.get("yearHigh"),
                        'year_low': crypto_data_fmp.get("yearLow")
                    }
                )


    #this part of data is comming from coin-paprika
    # Get ticker data from CoinGecko API
    # coin_data = get_ticker_for_a_specific_coin()
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
