from rest_framework import serializers
from .models import TwitterTweets


class TwitterTweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterTweets
        # fields = "__all__"
        exclude = ['id']
