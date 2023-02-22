from .models import ExplosureLinks
from screener.coin_by_id import coin_by_id


"""coin_by_id() is imported from screener. it has dispatched API response
        and providing us data here."""


def explorer_links_scripts():

    explorer_links_data = coin_by_id()
    links = explorer_links_data["links"]
    explorerlinks = links["explorer"]

    explosure_link_data = {
        "explorer_link_1": explorerlinks[0] if len(explorerlinks) > 0 else None,
        "explorer_link_2": explorerlinks[1] if len(explorerlinks) > 1 else None,
        "explorer_link_3": explorerlinks[2] if len(explorerlinks) > 2 else None,
        "explorer_link_4": explorerlinks[3] if len(explorerlinks) > 3 else None,
    }

    explosure_link_instance = ExplosureLinks()
    explosure_link_instance.explorer_link_1 = explosure_link_data["explorer_link_1"]
    explosure_link_instance.explorer_link_2 = explosure_link_data["explorer_link_2"]
    explosure_link_instance.explorer_link_3 = explosure_link_data["explorer_link_3"]
    explosure_link_instance.explorer_link_4 = explosure_link_data["explorer_link_4"]
    explosure_link_instance.save()


explorer_links_scripts()
