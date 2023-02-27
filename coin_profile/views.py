from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CoinProfile
from .serializers import CoinProfileSerializer


@api_view(["GET"])
def coin_profile_list(request):
    """
    Retrieve a list of all coin_profile_list objects and serialize them using the
    SocialLinksSerializer.
    
    Returns:
        Response: A serialized representation of the coin_profile_list objects.
    """
    coin_profiles = CoinProfile.objects.all()
    serializer = CoinProfileSerializer(coin_profiles, many=True)
    return Response(serializer.data)
