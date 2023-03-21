import re
import os
import pandas as pd
import pandasql as ps
import datetime
from coin_profile.models import CoinProfile
from calculate_performance import performance_change
from .models import PerformanceChange
from helper import call_api
API_KEY = os.environ.get('API_KEY')

def all_performance():
    symbols = CoinProfile.objects.values_list('symbol', flat=True)[3300:]
    for symbol in symbols:
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={API_KEY}'
        crypto_historical_api_data = call_api(url)
        # if crypto_historical_api_data is None and symbol.endswith('USD'):
        #     symbol = re.sub(r"USD", "", symbol)
        #     url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={API_KEY}'
        #     crypto_historical_api_data = call_api(url)
            
        if crypto_historical_api_data is not None:
            try:
                coin_symbol = CoinProfile.objects.get(symbol=symbol)
                symbol_data = []
                for row in crypto_historical_api_data["historical"]:
                    symbol_data.append({
                        "symbol":crypto_historical_api_data["symbol"],
                        "date": row["date"],
                        "close": row["close"]
                    })
                #Convert symbol_data into DataFrame
                historical_dataframe = pd.DataFrame(symbol_data)
                historical_dataframe["date"] = pd.to_datetime(historical_dataframe["date"])
                historical_dataframe["date"] = historical_dataframe["date"].dt.strftime("%Y-%m-%d")
                historical_dataframe.set_index("date", inplace=True)
                
                today = datetime.datetime.now()
                yesterday = today - datetime.timedelta(+1)
                
                #Weekly
                most_recent_week = yesterday - datetime.timedelta(days=7)
                week_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe "\
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_week.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                weekly_data = ps.sqldf(week_query, locals())
                
                #Monthly
                most_recent_month = yesterday - datetime.timedelta(days=30)
                month_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_month.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                monthly_data = ps.sqldf(month_query, locals())

                #Quarterly
                most_recent_qaurter = yesterday - datetime.timedelta(days=91)
                quarter_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_qaurter.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                quarter_data = ps.sqldf(quarter_query, locals())

                #Half-year
                most_recent_half_year = yesterday - datetime.timedelta(days=183)
                half_year_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_half_year.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                half_year_data = ps.sqldf(half_year_query, locals())

                #Yearly
                most_recent_year = yesterday - datetime.timedelta(days=365)
                year_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_year.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                full_year_data = ps.sqldf(year_query, locals())
                
                #YearToDate
                current_year = datetime.datetime.now().year
                first_date_of_current_year = datetime.datetime(current_year, 1, 1)
                year_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(first_date_of_current_year.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                year_to_date_data = ps.sqldf(year_query, locals())

                # Calculate-Performance
                weekly_performance = performance_change(weekly_data)
                monthly_performance = performance_change(monthly_data)
                quarterly_performance = performance_change(quarter_data)
                half_year_performance = performance_change(half_year_data)
                year_performance = performance_change(full_year_data)
                year_to_date_data = performance_change(year_to_date_data)

                performance_change_instance, created = PerformanceChange.objects.update_or_create(
                    symbol=coin_symbol,
                    defaults={
                        "weekly_percentage_change": weekly_performance,
                        "monthly_percentage_change": monthly_performance,
                        "quarterly_percentage_change": quarterly_performance,
                        "half_yearly_percentage_change": half_year_performance,
                        "yearly_percentage_change": year_performance,
                        'year_to_date':year_to_date_data
                    }
                )

            except Exception as e:
                pass

