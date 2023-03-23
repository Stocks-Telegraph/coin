from rest_framework import serializers
from .models import CryptoHistoricalData

class HistoricalTableDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoHistoricalData
        fields = ['date', 'open', 'high', 'low', 'close', 'volume']
        
        
class HistoricalChartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoHistoricalData
        fields = ['date', 'close']
