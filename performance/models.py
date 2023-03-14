from django.db import models
from coin_profile.models import CoinProfile
# Create your models here.
class PerformanceChange(models.Model):
    symbol = models.OneToOneField(CoinProfile, on_delete=models.CASCADE)
    weekly_percentage_change = models.FloatField(null=True)
    monthly_percentage_change = models.FloatField(null=True)
    quarterly_percentage_change = models.FloatField(null=True)
    half_yearly_percentage_change = models.FloatField(null=True)
    yearly_percentage_change = models.FloatField(null=True)
    year_to_date = models.FloatField(null=True)
    
    
    def __str__(self):
        return self.symbol.symbol
    class Meta:
        verbose_name_plural = 'Performance Change'