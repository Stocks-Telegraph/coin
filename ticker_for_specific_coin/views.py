from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TickerForSpecificCoin
from .serializers import TickerForSpecificCoinSerializer
from rest_framework import status

@api_view(["GET"])
def ticker_specific_coin(request):
    symbol = request.GET.get('symbol').upper()
    ticker_specific_coin_data = TickerForSpecificCoin.objects.filter(symbol__symbol=symbol)
    if not ticker_specific_coin_data.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TickerForSpecificCoinSerializer(ticker_specific_coin_data, many=True)
    return Response(serializer.data)
