from rest_framework import serializers
from .models import ExplosureLinks, SocialLinks


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"


class ExplosureLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExplosureLinks
        fields = "__all__"
