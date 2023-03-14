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
    symbols = CoinProfile.objects.values_list('symbol', flat=True)[40:55]    
    # symbols = ['ACTUSD']
    for symbol in symbols:
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={API_KEY}'
        crypto_historical_api_data = call_api(url)
        if crypto_historical_api_data is not None:
            try:
                coin_profile = CoinProfile.objects.get(symbol=symbol)
                print(coin_profile)
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
                
                #Calculate the weekly return
                most_recent_week = yesterday - datetime.timedelta(days=7)
                week_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe "\
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_week.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                weekly_data = ps.sqldf(week_query, locals())
                weekly_performance = performance_change(weekly_data)
                
                #Calculate the monthly return
                most_recent_month = yesterday - datetime.timedelta(days=30)
                month_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_month.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                monthly_data = ps.sqldf(month_query, locals())
                monthly_performance = performance_change(monthly_data)

                #Calculate the quarterly return
                most_recent_qaurter = yesterday - datetime.timedelta(days=91)
                quarter_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_qaurter.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                quarter_data = ps.sqldf(quarter_query, locals())
                quarterly_performance = performance_change(quarter_data)

                #Calculate the half-year return
                most_recent_half_year = yesterday - datetime.timedelta(days=183)
                half_year_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_half_year.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                half_year_data = ps.sqldf(half_year_query, locals())
                half_year_performance = performance_change(half_year_data)

                #Calculate the yearly return
                most_recent_year = yesterday - datetime.timedelta(days=365)
                year_query = "SELECT symbol, date, close " \
                        "FROM historical_dataframe " \
                        "WHERE date = '{}' OR date = '{}'".format(most_recent_year.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                full_year_data = ps.sqldf(year_query, locals())
                year_performance = performance_change(full_year_data)
                print(year_performance)
                # performance_change = PerformanceChange.objects.create(
                #         coin_profile=coin_profile,
                #         weekly_percentage_change=5,
                #         monthly_percentage_change=10,
                #         quarterly_percentage_change=15,
                #         half_yearly_percentage_change=20,
                #         yearly_percentage_change=25
                #                 )

                # # Save the instance
                # performance_change.save()
            except Exception as e:
                print(e)
        # return Response({'error': 'Something went wrong'})

