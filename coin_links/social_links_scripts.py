from .models import SocialLinks
from screener.coin_by_id import coin_by_id


def social_links_scripts():
    social_links_data = coin_by_id()
    links = social_links_data["links"]

    social_links_instance = SocialLinks()
    social_links_instance.facebook = links.get("facebook", [None])[0]
    social_links_instance.reddit = links.get("reddit", [None])[0]
    social_links_instance.source_code = links.get("source_code", [None])[0]
    social_links_instance.website = links.get("website", [None])[0]
    social_links_instance.youtube_link = links.get("youtube", [None])[0]
    social_links_instance.save()


social_links_scripts()
