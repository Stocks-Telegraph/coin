from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from coin_profile.models import CoinProfile
from django.db.models import Q

class CoinSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoinProfile
        fields = ["symbol","name"]


@api_view(['GET'])
def search_api(request, slug):
    if request.method == 'GET':
        coin_objects = CoinProfile.objects
        coins = coin_objects.filter(symbol__startswith=slug.upper()).order_by('symbol')
        if coins:
            pass
        else:
            coins = coin_objects.filter(name__icontains=slug).order_by('symbol')
        serializers = CoinSerializers(coins[:5], many=True)
        return Response(serializers.data)