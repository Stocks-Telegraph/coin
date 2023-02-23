from rest_framework import serializers
from .models import TickerForSpecificCoin


class TickerForSpecificCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = TickerForSpecificCoin
        fields = "__all__"
