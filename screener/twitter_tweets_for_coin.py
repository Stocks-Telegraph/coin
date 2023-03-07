import requests
from coin_profile.models import CoinProfile
def twitter_tweets_for_coin():
    """
    Retrieve Twitter data for a specific cryptocurrency.

    Uses CoinPaprika API to retrieve Twitter data for a
    specific cryptocurrency, identified by its `id`. 
    Returns:
        dict: A dictionary containing the Twitter data for the specified cryptocurrency.
    """
    # ids = CoinProfile.objects.values_list('coin_id', flat=True)
    ids = ["eth-ethereum"]
    for id in ids:
        url = f"https://api.coinpaprika.com/v1/coins/{id}/twitter"
        response = requests.get(url)
        response_data = response.json()
        return response_data


twitter_tweets_for_coin()
