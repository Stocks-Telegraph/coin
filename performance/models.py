from django.db import models
from coin_profile.models import CoinProfile
# Create your models here.
class PerformanceChange(models.Model):
    coin_profile = models.OneToOneField(CoinProfile, on_delete=models.CASCADE)
    weekly_percentage_change = models.IntegerField(null=True)
    monthly_percentage_change = models.IntegerField(null=True)
    quarterly_percentage_change = models.IntegerField(null=True)
    half_yearly_percentage_change = models.IntegerField(null=True)
    yearly_percentage_change = models.IntegerField(null=True)
    year_to_date = models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.coin_profile.symbol
    class Meta:
        verbose_name_plural = 'Performance Change'