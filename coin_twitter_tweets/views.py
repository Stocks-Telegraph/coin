from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TwitterTweets
from .serializers import TwitterTweetsSerializer


@api_view(["GET"])
def twitter_tweet_list(request):
    """
    Retrieve a list of all twitter_tweet_list objects and serialize them using the
    SocialLinksSerializer.
    
    Returns:
        Response: A serialized representation of the twitter_tweet_list objects.
    """
    twitter_tweets = TwitterTweets.objects.all()
    serializer = TwitterTweetsSerializer(twitter_tweets, many=True)
    return Response(serializer.data)
