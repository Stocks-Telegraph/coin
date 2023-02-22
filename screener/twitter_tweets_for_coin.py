import requests
from coin_twitter_tweets.models import TwitterTweets


def twitter_tweets_for_coin():
    ids = ['matic-polygon']
    for id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{id}/twitter'
        response = requests.get(url)
        response_data = response.json()
        return response_data     

twitter_tweets_for_coin()