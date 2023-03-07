from django.db import models
from coin_profile.models import CoinProfile

# Create your models here.
class Today_OHLC(models.Model):
    symbol = models.ForeignKey(CoinProfile, to_field="symbol", on_delete=models.CASCADE)
    time_open = models.CharField(max_length=120)
    time_close = models.CharField(max_length=120)
    open = models.FloatField(null=True)
    high = models.FloatField(null=True)
    low = models.FloatField(null=True)
    close = models.FloatField(null=True)
    volume = models.IntegerField(null=True)
    market_cap = models.IntegerField(null=True)

    def __str__(self):
        return self.symbol.symbol

    class Meta:
        verbose_name_plural = "Coin-today-data"
