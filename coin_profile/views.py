from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CoinProfile
from .serializers import CoinProfileSerializer
from rest_framework import status

@api_view(["GET"])
def coin_profile_list(request):
    """
    Retrieve a list of all coin_profile_list objects and serialize them using the
    SocialLinksSerializer.
    
    Returns:
        Response: A serialized representation of the coin_profile_list objects.
    """
    symbol = request.GET.get('symbol').upper()
    coin_profiles = CoinProfile.objects.filter(symbol=symbol)
    if not coin_profiles.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CoinProfileSerializer(coin_profiles, many=True)
    return Response(serializer.data)
