from screener.get_ticker_for_a_specific_coin import get_ticker_for_a_specific_coin
from .models import TickerForSpecificCoin


def ticker_for_a_spec_coin():
    coin_data = get_ticker_for_a_specific_coin()
    usd_data = coin_data.get("quotes", {}).get("USD", {})

    specific_coin_instance = TickerForSpecificCoin()

    specific_coin_instance.coin_id = coin_data.get("id")
    specific_coin_instance.name = coin_data.get("name")
    specific_coin_instance.symbol = coin_data.get("symbol")
    specific_coin_instance.rank = coin_data.get("rank")
    specific_coin_instance.circulating_supply = coin_data.get("circulating_supply")
    specific_coin_instance.total_supply = coin_data.get("total_supply")
    specific_coin_instance.max_supply = coin_data.get("max_supply")
    specific_coin_instance.beta_value = coin_data.get("beta_value")
    specific_coin_instance.first_data_at = coin_data.get("first_data_at")
    specific_coin_instance.last_updated = coin_data.get("last_updated")

    specific_coin_instance.price = usd_data.get("price")
    specific_coin_instance.volume_24h = usd_data.get("volume_24h")
    specific_coin_instance.volume_24h_change_24h = usd_data.get("volume_24h_change_24h")
    specific_coin_instance.market_cap = usd_data.get("market_cap")
    specific_coin_instance.market_cap_change_24h = usd_data.get("market_cap_change_24h")
    specific_coin_instance.percent_change_15m = usd_data.get("percent_change_15m")
    specific_coin_instance.percent_change_30m = usd_data.get("percent_change_30m")
    specific_coin_instance.percent_change_1h = usd_data.get("percent_change_1h")
    specific_coin_instance.percent_change_6h = usd_data.get("percent_change_6h")
    specific_coin_instance.percent_change_12h = usd_data.get("percent_change_12h")
    specific_coin_instance.percent_change_24h = usd_data.get("percent_change_24h")
    specific_coin_instance.percent_change_7d = usd_data.get("percent_change_7d")
    specific_coin_instance.percent_change_30d = usd_data.get("percent_change_30d")
    specific_coin_instance.percent_change_1y = usd_data.get("percent_change_1y")
    specific_coin_instance.ath_price = usd_data.get("ath_price")
    specific_coin_instance.ath_date = usd_data.get("ath_date")
    specific_coin_instance.percent_from_price_ath = usd_data.get(
        "percent_from_price_ath"
    )

    specific_coin_instance.save()
