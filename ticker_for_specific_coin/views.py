from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TickerForSpecificCoin
from .serializers import TickerForSpecificCoinSerializer
from rest_framework import status
from coin_profile.models import CoinProfile

@api_view(["GET"])
def data_of_crypto(request):
    symbol = request.GET.get("symbol", "").upper()
    if symbol:
        ticker_specific_coin_data = TickerForSpecificCoin.objects.filter(
            symbol__symbol=symbol
        )
    else:
        ticker_specific_coin_data = TickerForSpecificCoin.objects.all()
    if not ticker_specific_coin_data.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TickerForSpecificCoinSerializer(ticker_specific_coin_data, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def create_ticker(request):
#     symbol = request.data.get('symbol')
#     circulating_supply = request.data.get('circulating_supply')
#     total_supply = request.data.get('total_supply')
#     max_supply = request.data.get('max_supply')
#     beta_value = request.data.get('beta_value')
#     first_data_at = request.data.get('first_data_at')
#     last_updated = request.data.get('last_updated')
#     price = request.data.get('price')
#     volume_24h = request.data.get('volume_24h')
#     volume_24h_change_24h = request.data.get('volume_24h_change_24h')
#     market_cap = request.data.get('market_cap')
#     market_cap_change_24h = request.data.get('market_cap_change_24h')
#     change_percentage = request.data.get('change_percentage')
#     year_high = request.data.get('year_high')
#     year_low = request.data.get('year_low')

#     try:
#         coin_profile = CoinProfile.objects.get(symbol=symbol)
#         ticker = TickerForSpecificCoin.objects.create(
#             symbol=coin_profile,
#             circulating_supply=circulating_supply,
#             total_supply=total_supply,
#             max_supply=max_supply,
#             beta_value=beta_value,
#             first_data_at=first_data_at,
#             last_updated=last_updated,
#             price=price,
#             volume_24h=volume_24h,
#             volume_24h_change_24h=volume_24h_change_24h,
#             market_cap=market_cap,
#             market_cap_change_24h=market_cap_change_24h,
#             change_percentage=change_percentage,
#             year_high=year_high,
#             year_low=year_low,
#         )
#         return Response({'message': 'Ticker created successfully'}, status=status.HTTP_201_CREATED)
#     except CoinProfile.DoesNotExist:
#         return Response({'error': 'Invalid symbol'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
#post below from postman
"""
{
    "symbol": "BTC",
    "circulating_supply": 18500000,
    "total_supply": 21000000,
    "max_supply": 21000000,
    "beta_value": 0.5,
    "first_data_at": "2021-01-01T00:00:00Z",
    "last_updated": "2021-03-10T10:00:00Z",
    "price": 50000,
    "volume_24h": 50000000000,
    "volume_24h_change_24h": 1.2,
    "market_cap": 925000000000,
    "market_cap_change_24h": 0.8,
    "change_percentage": 1.5,
    "year_high": 65000,
    "year_low": 30000
}
make sure to change symbol"""
