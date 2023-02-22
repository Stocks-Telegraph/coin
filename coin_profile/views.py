from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CoinProfile
from .serializers import CoinProfileSerializer

@api_view(['GET'])
def coin_profile_list(request):
    coin_profiles = CoinProfile.objects.all()
    serializer = CoinProfileSerializer(coin_profiles, many=True)
    return Response(serializer.data)

