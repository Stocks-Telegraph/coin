from rest_framework import serializers
from .models import PerformanceChange


class PerformanceChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerformanceChange
        exclude = ["id"]