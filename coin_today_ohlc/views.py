from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Today_OHLC
from rest_framework import status
from .serializers import Today_OHLCSerializer


@api_view(["GET"])
def today_OHLC_list(request):
    symbol = request.GET.get("symbol").upper()
    today_ohlc_data = Today_OHLC.objects.filter(symbol__symbol=symbol)
    if not today_ohlc_data.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = Today_OHLCSerializer(today_ohlc_data, many=True)
    return Response(serializer.data)
