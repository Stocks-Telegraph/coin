from coin_profile.models import CoinProfile
from .models import SocialLinks

from .api_scripts.coinpaprika_social_links import coinpaprika_social_links

def social_links_scripts():
    social_links_response = coinpaprika_social_links()
    for all_links in social_links_response:
            coin_name = all_links["id"]
            try:
                all_social_links = all_links["Social_links"]
                coin_profile = CoinProfile.objects.get(coin_id=coin_name)
                SocialLinks.objects.update_or_create(
                    symbol=coin_profile,
                    defaults={
                        "facebook": all_social_links.get("facebook", [None])[0],
                        "reddit": all_social_links.get("reddit", [None])[0],
                        "source_code": all_social_links.get("source_code", [None])[0],
                        "website": all_social_links.get("website", [None])[0],
                        "youtube_link": all_social_links.get("youtube", [None])[0]
                    }
                )
            
            except:
                pass

# social_links_scripts()
