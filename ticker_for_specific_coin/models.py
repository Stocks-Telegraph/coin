from django.db import models

# Create your models here.
class TickerForSpecificCoin(models.Model):
    coin_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)
    rank = models.IntegerField()
    circulating_supply = models.IntegerField()
    total_supply = models.IntegerField(null=True)
    max_supply = models.IntegerField(null=True)
    beta_value = models.FloatField(null=True)
    first_data_at = models.DateTimeField()
    last_updated = models.DateTimeField()
    price = models.BigIntegerField()
    volume_24h = models.BigIntegerField()
    volume_24h_change_24h = models.FloatField()
    market_cap = models.FloatField()
    market_cap_change_24h = models.FloatField()
    percent_change_15m = models.FloatField()
    percent_change_30m = models.FloatField()
    percent_change_1h = models.FloatField()
    percent_change_6h = models.FloatField()
    percent_change_12h = models.FloatField()
    percent_change_24h = models.FloatField()
    percent_change_7d = models.FloatField()
    percent_change_30d = models.FloatField()
    percent_change_1y = models.FloatField()
    ath_price = models.BigIntegerField()
    ath_date = models.DateTimeField()
    percent_from_price_ath = models.FloatField()

    def __str__(self):
        return self.coin_id
    class Meta:
        verbose_name_plural = "ticker for a specific coin"
