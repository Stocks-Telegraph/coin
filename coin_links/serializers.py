from rest_framework import serializers
from .models import ExplosureLinks, SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    """
    This serializer converts SocialLinks model instances to a JSON representation,
    and is used for parsing and validating incoming data from API requests.

    The special string value '__all__' will include all fields.
    """
    class Meta:
        model = SocialLinks
        fields = "__all__"


class ExplosureLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExplosureLinks
        fields = "__all__"
