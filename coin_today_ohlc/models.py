from django.db import models
from coin_profile.models import CoinProfile

# Create your models here.
class Today_OHLC(models.Model):
    symbol = models.ForeignKey(CoinProfile, to_field='symbol', on_delete=models.CASCADE)
    time_open = models.CharField(max_length=120)
    time_close = models.CharField(max_length=120)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    market_cap = models.IntegerField()

    def __str__(self):
        return f"{self.time_open} - {self.time_close}"

    class Meta:
        verbose_name_plural = "get_today_OHLC"
