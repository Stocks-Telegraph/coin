from screener.get_ticker_for_a_specific_coin import get_ticker_for_a_specific_coin
from .models import TickerForSpecificCoin


def ticker_for_a_spec_coin():
    get_ticker_for_a_specific_coin_data = get_ticker_for_a_specific_coin()
    get_ticker_for_a_specific_coin_data_quote = get_ticker_for_a_specific_coin_data['quotes']['USD']
    
    specific_coin_instance = TickerForSpecificCoin()
    
    
    specific_coin_instance.coin_id = get_ticker_for_a_specific_coin_data["id"]
    specific_coin_instance.name = get_ticker_for_a_specific_coin_data["name"]
    specific_coin_instance.symbol = get_ticker_for_a_specific_coin_data["symbol"]
    specific_coin_instance.rank = get_ticker_for_a_specific_coin_data["rank"]
    specific_coin_instance.circulating_supply = get_ticker_for_a_specific_coin_data["circulating_supply"]
    specific_coin_instance.total_supply = get_ticker_for_a_specific_coin_data["total_supply"]
    specific_coin_instance.max_supply = get_ticker_for_a_specific_coin_data["max_supply"]
    specific_coin_instance.beta_value = get_ticker_for_a_specific_coin_data["beta_value"]
    specific_coin_instance.first_data_at =get_ticker_for_a_specific_coin_data["first_data_at"]
    specific_coin_instance.last_updated = get_ticker_for_a_specific_coin_data["last_updated"]
    
    specific_coin_instance.price = get_ticker_for_a_specific_coin_data_quote["price"]
    specific_coin_instance.volume_24h = get_ticker_for_a_specific_coin_data_quote["volume_24h"]
    specific_coin_instance.volume_24h_change_24h = get_ticker_for_a_specific_coin_data_quote["volume_24h_change_24h"]
    specific_coin_instance.market_cap = get_ticker_for_a_specific_coin_data_quote["market_cap"]
    specific_coin_instance.market_cap_change_24h = get_ticker_for_a_specific_coin_data_quote["market_cap_change_24h"]
    specific_coin_instance.percent_change_15m = get_ticker_for_a_specific_coin_data_quote["percent_change_15m"]
    specific_coin_instance.percent_change_30m = get_ticker_for_a_specific_coin_data_quote["percent_change_30m"]
    specific_coin_instance.percent_change_1h = get_ticker_for_a_specific_coin_data_quote["percent_change_1h"]
    specific_coin_instance.percent_change_6h = get_ticker_for_a_specific_coin_data_quote["percent_change_6h"]
    specific_coin_instance.percent_change_12h = get_ticker_for_a_specific_coin_data_quote["percent_change_12h"]
    specific_coin_instance.percent_change_24h = get_ticker_for_a_specific_coin_data_quote["percent_change_24h"]
    specific_coin_instance.percent_change_7d = get_ticker_for_a_specific_coin_data_quote["percent_change_7d"]
    specific_coin_instance.percent_change_30d = get_ticker_for_a_specific_coin_data_quote["percent_change_30d"]
    specific_coin_instance.percent_change_1y = get_ticker_for_a_specific_coin_data_quote["percent_change_1y"]
    specific_coin_instance.ath_price = get_ticker_for_a_specific_coin_data_quote["ath_price"]
    specific_coin_instance.ath_date = get_ticker_for_a_specific_coin_data_quote["ath_date"]
    specific_coin_instance.percent_from_price_ath =get_ticker_for_a_specific_coin_data_quote["percent_from_price_ath"]
    
    
    specific_coin_instance.save()
    
