from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PerformanceChange
from rest_framework import status
from .serializers import PerformanceChangeSerializer


@api_view(["GET"])
def performance_change(request):
    symbol = request.GET.get("symbol", "").upper()
    if symbol:
        today_ohlc_data = PerformanceChange.objects.filter(symbol__symbol=symbol)
    else:
        today_ohlc_data = PerformanceChange.objects.all()
    if not today_ohlc_data.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PerformanceChangeSerializer(today_ohlc_data, many=True)
    return Response(serializer.data)
