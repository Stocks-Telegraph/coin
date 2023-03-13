import requests
import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
import pandasql as ps
import datetime
from calculate_performance import performance_change
from coin_profile.models import CoinProfile
API_KEY = os.environ.get('API_KEY')

def all_performance():
    # symbols = CoinProfile.objects.values_list('symbol', flat=True)[70:75]    
    symbols = ['btcusd']
    for symbol in symbols:
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            crypto_historical_api_data = response.json()
            if crypto_historical_api_data is not None:
                try:
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

                    # df_weekly = performance_change(historical_dataframe, 'price', 'W')
                    # df_monthly = performance_change(historical_dataframe, 'price', 'M')
                    # df_half_yearly = performance_change(historical_dataframe, 'price', '6M')
                    # df_yearly = performance_change(historical_dataframe, 'price', 'Y')
                    
                    today = datetime.datetime.now()
                    yesterday = today - datetime.timedelta(+1)
                    # Calculate the weekly return
                    most_recent_week = yesterday - datetime.timedelta(days=7)
                    week_query = "SELECT symbol, date, close " \
                            "FROM historical_dataframe "\
                            "WHERE date = '{}' OR date = '{}'".format(most_recent_week.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
                    weekly_data = ps.sqldf(week_query, locals())
                    weekly_performance = performance_change(weekly_data)
                    print(symbol,weekly_performance)
                
                except Exception as e:
                    pass

        # #Calculate the monthly return
        # most_recent_month = yesterday - datetime.timedelta(days=30)
        # month_query = "SELECT symbol, date, close " \
        #         "FROM historical_dataframe " \
        #         "WHERE date = '{}' OR date = '{}'".format(most_recent_month.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
        # month_df = ps.sqldf(month_query, locals())
        # monthly_performance = performance_calculation.performance_change(month_df)
        # print(monthly_performance)
        
        # #Calculate the quarterly return
        # most_recent_qaurter = yesterday - datetime.timedelta(days=91)
        # quarter_query = "SELECT symbol, date, close " \
        #         "FROM historical_dataframe " \
        #         "WHERE date = '{}' OR date = '{}'".format(most_recent_qaurter.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
        # quarter_df = ps.sqldf(quarter_query, locals())
        # quarterly_performance = performance_calculation.performance_change(quarter_df)
        # print(quarterly_performance)
        
        # #Calculate the half-year return
        # most_recent_half_year = yesterday - datetime.timedelta(days=183)
        # half_year_query = "SELECT symbol, date, close " \
        #         "FROM historical_dataframe " \
        #         "WHERE date = '{}' OR date = '{}'".format(most_recent_half_year.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
        # half_year_df = ps.sqldf(half_year_query, locals())
        # half_year_performance = performance_calculation.performance_change(half_year_df)
        # print(half_year_performance)
        
        # #Calculate the yearly return
        # most_recent_year = yesterday - datetime.timedelta(days=365)
        # year_query = "SELECT symbol, date, close " \
        #         "FROM historical_dataframe " \
        #         "WHERE date = '{}' OR date = '{}'".format(most_recent_year.strftime("%Y-%m-%d"), yesterday.strftime("%Y-%m-%d"))
        # full_year_df = ps.sqldf(year_query, locals())
        # year_performance = performance_calculation.performance_change(full_year_df)
        # print(year_performance)
        
    # return Response({'error': 'Something went wrong'})
