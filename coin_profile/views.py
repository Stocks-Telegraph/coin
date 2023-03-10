from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CoinProfile
from .serializers import CoinProfileSerializer
from rest_framework import status


@api_view(["GET"])
def coin_profile(request):
    symbol = request.GET.get("symbol", "").upper()
    if symbol:
        coin_profiles = CoinProfile.objects.filter(symbol=symbol)
    else:
        coin_profiles = CoinProfile.objects.all()
    if not coin_profiles.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CoinProfileSerializer(coin_profiles, many=True)
    return Response(serializer.data)
