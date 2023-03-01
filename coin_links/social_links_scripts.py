from .models import SocialLinks
from screener.coin_by_id import coin_by_id


def social_links_scripts():
    """
    coin_by_id() is imported from screener. it contains data that has taken from dispatching API response,
    Get that data here, format it accordingly and save it to db
    """
    social_links = coin_by_id()
    for social_links_data in social_links:
        print(social_links_data)
        if "links" not in social_links_data:
            continue
        
        links = social_links_data["links"]

        social_links_instance = SocialLinks()
        social_links_instance.facebook = links.get("facebook", [None])[0]
        social_links_instance.reddit = links.get("reddit", [None])[0]
        social_links_instance.source_code = links.get("source_code", [None])[0]
        social_links_instance.website = links.get("website", [None])[0]
        social_links_instance.youtube_link = links.get("youtube", [None])[0]
        social_links_instance.save()


social_links_scripts()
