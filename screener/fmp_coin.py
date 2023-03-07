import requests

def fmp_api_coin():
        """
        Get all the coins name and symbol from this endpoint,combine and format them and make coin_id,
        Once you generate coin_id , create the instance of Model and save these three attribute inside it.
        """
        
        url = "https://financialmodelingprep.com/api/v3/quotes/crypto?apikey=76b77192c1a4d71a0ac45394989d009e"
        response = requests.get(url)
        response_data = response.json()
        return response_data
 
fmp_api_coin()
        