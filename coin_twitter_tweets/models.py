from django.db import models

# Create your models here.
class TwitterTweets(models.Model):
    date = models.DateTimeField(auto_now=True)
    user_name = models.CharField(max_length=120) 
    user_image_link = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    is_retweet = models.BooleanField()
    retweet_count = models.IntegerField()
    like_count = models.IntegerField()
    status_id = models.CharField(max_length=120)
    media_link = models.CharField(max_length=120,null=True)
    youtube_link = models.CharField(max_length=120, null=True)
    
    
    def __str__(self):
        return f'{self.user_name}'
    
    class Meta:
        verbose_name_plural = "Twitter Tweets"