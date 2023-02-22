from rest_framework import serializers
from .models import CoinProfile

class CoinProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinProfile
        fields = '__all__'
