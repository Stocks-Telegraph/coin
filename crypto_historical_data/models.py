# from django.db import models
# from coin_profile.models import CoinProfile

# class CryptoHistoricalData(models.Model):
#     symbol = models.ForeignKey(CoinProfile, to_field='symbol', on_delete=models.CASCADE)
#     date = models.DateField()
#     open = models.FloatField()
#     high = models.FloatField()
#     low = models.FloatField()
#     close = models.FloatField()
#     adj_close = models.FloatField()
#     volume = models.BigIntegerField()
#     unadjusted_volume = models.BigIntegerField()
#     change = models.FloatField()
#     change_percent = models.FloatField()
#     vwap = models.FloatField()
#     change_over_time = models.FloatField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.symbol.symbol


#     class Meta:
#         verbose_name_plural = "Crypto-Historical-Data"
