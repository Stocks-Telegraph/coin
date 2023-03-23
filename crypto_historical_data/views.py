from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CryptoHistoricalData
from .serializers import HistoricalChartDataSerializer, HistoricalTableDataSerializer

@api_view(['GET'])
def historical_chart(request, symbol):
    symbol = symbol.upper()
    queryset = CryptoHistoricalData.objects.filter(symbol__symbol=symbol).order_by('date')
    serializer = HistoricalChartDataSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def historical_table(request, symbol):
    symbol = symbol.upper()
    queryset = CryptoHistoricalData.objects.filter(symbol__symbol=symbol).order_by('date')
    serializer = HistoricalTableDataSerializer(queryset, many=True)
    return Response(serializer.data)