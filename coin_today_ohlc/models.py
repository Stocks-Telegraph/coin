from django.db import models
from coin_profile.models import CoinProfile

# Create your models here.
class Today_OHLC(models.Model):
    symbol = models.ForeignKey(CoinProfile, to_field="symbol", on_delete=models.CASCADE)
    open = models.FloatField(null=True)
    previousClose = models.FloatField(null=True)
    day_high = models.FloatField(null=True)
    day_low = models.FloatField(null=True)
    year_high = models.FloatField(null=True)
    year_low = models.FloatField(null=True)
    price_avg50 = models.FloatField(null=True)
    price_avg200 = models.FloatField(null=True)
    volume = models.IntegerField(null=True)
    avg_volume = models.IntegerField(null=True)
    market_cap = models.IntegerField(null=True)
    # timestamp = models.IntegerField(null=True)
    
    def __str__(self):
        return self.symbol.symbol

    class Meta:
        verbose_name_plural = "Coin-today-data"
