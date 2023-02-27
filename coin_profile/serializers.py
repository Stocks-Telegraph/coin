from rest_framework import serializers
from .models import CoinProfile


class CoinProfileSerializer(serializers.ModelSerializer):
    """
    This serializer converts CoinProfileSerializer model instances to a JSON representation,
    and is used for parsing and validating incoming data from API requests.

    The special string value '__all__' will include all fields.
    """
    class Meta:
        model = CoinProfile
        fields = "__all__"
