from django.db import models
from coin_profile.models import CoinProfile

# Create your models here.
class TwitterTweets(models.Model):
    symbol = models.ForeignKey(CoinProfile, to_field='symbol', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=120)
    user_image_link = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    is_retweet = models.BooleanField()
    retweet_count = models.IntegerField()
    like_count = models.IntegerField()
    status_id = models.CharField(max_length=120)
    media_link = models.CharField(max_length=120, null=True)
    youtube_link = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.symbol.symbol

    class Meta:
        verbose_name_plural = "Twitter-tweets-regarding-a-coin"
