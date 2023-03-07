from rest_framework import serializers
from .models import ExplorerLinks, SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    """
    This serializer converts SocialLinks model instances to a JSON representation,
    and is used for parsing and validating incoming data from API requests.

    The special string value '__all__' will include all fields.
    """

    class Meta:
        model = SocialLinks
        exclude = ["id"]
        # fields = "__all__"


class ExplorerLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExplorerLinks
        exclude = ["id"]
        # fields = "__all__"
