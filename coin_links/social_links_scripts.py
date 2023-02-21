import requests
from .models import SocialLinks

def social_links_scripts():
    ids = ['eth-ethereum','usdt-tether']
    for id in ids:
        url = f'https://api.coinpaprika.com/v1/coins/{id}'
        response = requests.get(url)
        response_data = response.json()
        links = response_data['links']
          
        social_links_instance = SocialLinks()
        social_links_instance.facebook= links['facebook'][0]
        social_links_instance.reddit= links['reddit'][0]
        social_links_instance.source_code= links['source_code'][0]
        social_links_instance.website= links['website'][0]
        social_links_instance.youtube_link= links['youtube'][0]
        social_links_instance.save()
        break
        

social_links_scripts()