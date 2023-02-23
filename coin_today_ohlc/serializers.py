from rest_framework import serializers
from .models import Today_OHLC


class Today_OHLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Today_OHLC
        fields = "__all__"
