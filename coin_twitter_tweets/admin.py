from django.contrib import admin
from .models import TwitterTweets
class TwitterTweetsAdmin(admin.ModelAdmin):
    list_per_page = 12

admin.site.register(TwitterTweets, TwitterTweetsAdmin)
