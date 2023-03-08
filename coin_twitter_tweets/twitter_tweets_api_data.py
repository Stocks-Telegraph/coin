from .models import TwitterTweets
from coin_profile.models import CoinProfile

from helper import call_api

def twitter_tweets_api_data():
    ids = CoinProfile.objects.values_list('coin_id', flat=True)[:20]
    for coin_id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{coin_id}/twitter"
        response_data = call_api(url)
        print('response', response_data)
        if response_data is not None:
            print(response_data)
            for twitter_response_data in response_data:  
                try:
                    # coin_profile = CoinProfile.objects.get(symbol=id)
                    # print('Coin-Profile',coin_profile)
                    twitter_tweets_instance, created = TwitterTweets.objects.update_or_create(
                        symbol=coin_id,
                        date=twitter_response_data["date"],
                        user_name=twitter_response_data["user_name"],
                        user_image_link=twitter_response_data["user_image_link"],
                        status=twitter_response_data["status"],
                        is_retweet=twitter_response_data["is_retweet"],
                        retweet_count=twitter_response_data["retweet_count"],
                        like_count=twitter_response_data["like_count"],
                        status_id=twitter_response_data["status_id"],
                    )
                except CoinProfile.DoesNotExist:
                    continue


        else:
            pass
          
        


twitter_tweets_api_data()
