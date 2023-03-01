from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TwitterTweets
from .serializers import TwitterTweetsSerializer
from rest_framework import status

@api_view(["GET"])
def twitter_tweet_list(request):
    """
    Retrieve a list of all twitter_tweet_list objects and serialize them using the
    SocialLinksSerializer.
    
    Returns:
        Response: A serialized representation of the twitter_tweet_list objects.
    """
    symbol = request.GET.get('symbol').upper()
    twitter_tweets = TwitterTweets.objects.filter(symbol__symbol=symbol)
    if not twitter_tweets.exists():
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TwitterTweetsSerializer(twitter_tweets, many=True)
    return Response(serializer.data)
