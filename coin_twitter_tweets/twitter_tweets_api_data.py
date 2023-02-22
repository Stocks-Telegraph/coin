from .models import TwitterTweets
from screener.twitter_tweets_for_coin import twitter_tweets_for_coin


def twitter_tweets_api_data():
    twitter_tweets_data = twitter_tweets_for_coin()

    for twitter_response_data in twitter_tweets_data:
        twitter_tweets_instance = TwitterTweets()
        twitter_tweets_instance.date = twitter_response_data["date"]
        twitter_tweets_instance.user_name = twitter_response_data["user_name"]
        twitter_tweets_instance.user_image_link = twitter_response_data[
            "user_image_link"
        ]
        twitter_tweets_instance.status = twitter_response_data["status"]
        twitter_tweets_instance.is_retweet = twitter_response_data["is_retweet"]
        twitter_tweets_instance.retweet_count = twitter_response_data["retweet_count"]
        twitter_tweets_instance.like_count = twitter_response_data["like_count"]
        twitter_tweets_instance.status_id = twitter_response_data["status_id"]

        twitter_tweets_instance.save()
        break


# twitter_tweets_api_data()
