from django.db import models
from coin_profile.models import CoinProfile

class CryptoHistoricalData(models.Model):
    symbol = models.ForeignKey(CoinProfile, to_field='symbol', on_delete=models.CASCADE)
    date = models.DateField()
    open = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    close = models.FloatField(null=True)
    volume = models.BigIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.symbol.symbol} - {self.date}'
    class Meta:
        verbose_name_plural = "Crypto-Historical-Data"
