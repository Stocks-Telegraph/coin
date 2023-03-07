from django.db import models
from coin_profile.models import CoinProfile
# Create your models here.
class TickerForSpecificCoin(models.Model):
    # coin_id = models.CharField(max_length=100)
    # name = models.CharField(max_length=100)
    symbol = models.ForeignKey(CoinProfile, to_field='symbol', on_delete=models.CASCADE)
    circulating_supply = models.IntegerField(null=True)
    total_supply = models.IntegerField(null=True)
    max_supply = models.IntegerField(null=True)
    beta_value = models.FloatField(null=True)
    first_data_at = models.DateTimeField(null=True)
    last_updated = models.DateTimeField(null=True)
    price = models.BigIntegerField() #Take This From Fmp
    volume_24h = models.BigIntegerField(null=True)
    volume_24h_change_24h = models.FloatField(null=True)
    market_cap = models.FloatField(null=True)
    market_cap_change_24h = models.FloatField(null=True)
    change_percentage = models.FloatField(null=True)
    # percent_change_15m = models.FloatField()
    # percent_change_30m = models.FloatField()
    # percent_change_1h = models.FloatField()
    # percent_change_6h = models.FloatField()
    # percent_change_12h = models.FloatField()
    # percent_change_24h = models.FloatField()
    # percent_change_7d = models.FloatField()
    # percent_change_30d = models.FloatField()
    # percent_change_1y = models.FloatField()
    year_high = models.FloatField() 
    year_low = models.FloatField() 
    # ath_price = models.BigIntegerField(null=True)
    # ath_date = models.DateTimeField(null=True)
    # percent_from_price_ath = models.FloatField()

    def __str__(self):
        return self.symbol.symbol


    class Meta:
        """
        Human-readable name for the object(s)
        that will be used in the Django admin interface. 
        """
        verbose_name_plural = "ticker for a specific coin"
