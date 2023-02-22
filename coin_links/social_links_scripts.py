import requests
from .models import SocialLinks

def social_links_scripts():
    ids = ['btc-bitcoin','eth-ethereum','busd-binance-usd','ada-cardano']
    for id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{id}'
        response = requests.get(url)
        response_data = response.json()
        links = response_data['links']
          
        social_links_instance = SocialLinks()
        social_links_instance.facebook= links.get('facebook', [None])[0]
        social_links_instance.reddit= links.get('reddit', [None])[0]
        social_links_instance.source_code= links.get('source_code', [None])[0]
        social_links_instance.website= links.get('website', [None])[0]
        social_links_instance.youtube_link= links.get('youtube', [None])[0]
        social_links_instance.save() 

# social_links_scripts()