from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TwitterTweets
from .serializers import TwitterTweetsSerializer

@api_view(['GET'])
def twitter_tweet_list(request):
    twitter_tweets = TwitterTweets.objects.all()
    serializer = TwitterTweetsSerializer(twitter_tweets, many=True)
    return Response(serializer.data)
    
