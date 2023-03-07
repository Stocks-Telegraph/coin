from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Today_OHLC
from rest_framework import status
from .serializers import Today_OHLCSerializer
from django.shortcuts import get_object_or_404


@api_view(["GET"])
def today_OHLC_list(request):
    """
    Retrieve a list of all today_OHLC_list objects and serialize them using the
    SocialLinksSerializer.

    Returns:
        Response: A serialized representation of the today_OHLC_list objects.
    """
    symbol = request.GET.get("symbol").upper()
    today_ohlc_data = Today_OHLC.objects.filter(symbol__symbol=symbol)
    if not today_ohlc_data.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = Today_OHLCSerializer(today_ohlc_data, many=True)
    return Response(serializer.data)
