from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TwitterTweets
from .serializers import TwitterTweetsSerializer
from rest_framework import status


@api_view(["GET"])
def twitter_tweet_list(request):
    symbol = request.GET.get("symbol", "").upper()
    if symbol:
        twitter_tweets = TwitterTweets.objects.filter(symbol__symbol=symbol)
    else:
        twitter_tweets = TwitterTweets.objects.all()
    if not twitter_tweets.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TwitterTweetsSerializer(twitter_tweets, many=True)
    return Response(serializer.data)
