from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Today_OHLC
from .serializers import Today_OHLCSerializer


@api_view(["GET"])
def today_OHLC_list(request):
    """
    Retrieve a list of all today_OHLC_list objects and serialize them using the
    SocialLinksSerializer.
    
    Returns:
        Response: A serialized representation of the today_OHLC_list objects.
    """
    coin_profiles = Today_OHLC.objects.all()
    serializer = Today_OHLCSerializer(coin_profiles, many=True)
    return Response(serializer.data)
