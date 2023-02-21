import requests
import pandas as pd


def twitter_tweets_for_coin():
    ids = ['usdt-tether','btc-bitcoin']
    for id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{id}/twitter'
        response = requests.get(url)
        response_data = response.json()
       
        # for twitter_tweets in response_data:
        #     return twitter_tweets
            
twitter_tweets_for_coin()