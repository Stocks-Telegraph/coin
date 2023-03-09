from rest_framework import serializers
from .models import ExplorerLinks, SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        exclude = ["id"]
        # fields = "__all__"


class ExplorerLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExplorerLinks
        exclude = ["id"]
        # fields = "__all__"
