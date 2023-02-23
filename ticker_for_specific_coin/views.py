from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TickerForSpecificCoin
from .serializers import TickerForSpecificCoinSerializer


@api_view(["GET"])
def ticker_specific_coin(request):
    twitter_tweets = TickerForSpecificCoin.objects.all()
    serializer = TickerForSpecificCoinSerializer(twitter_tweets, many=True)
    return Response(serializer.data)
