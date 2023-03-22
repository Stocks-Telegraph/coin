import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from helper import call_api

api_key = os.environ.get("API_KEY")

def get_historical_data(symbol):
    url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={api_key}'
    response_data = call_api(url)

    return response_data['historical']

@api_view(['GET'])
def historical_chart(request, symbol):
    historical_data = get_historical_data(symbol)

    all_historical_chart_data = []
    for historical_chart_data in historical_data:
        all_historical_chart_data.append({
            'date': historical_chart_data['date'],
            'close': historical_chart_data['close']
        })

    return Response(all_historical_chart_data)


@api_view(['GET'])
def historical_table(request, symbol):
    if symbol:
        historical_data = get_historical_data(symbol)

        all_historical_table_data = []
        for historical_table_data in historical_data:
            all_historical_table_data.append({
                'date': historical_table_data['date'],
                'open': historical_table_data['open'],
                'high': historical_table_data['high'],
                'low': historical_table_data['low'],
                'close': historical_table_data['close'],
                'volume': historical_table_data['volume']
            })

        return Response(all_historical_table_data)
    else:
        return Response('Please Pass symbol')
