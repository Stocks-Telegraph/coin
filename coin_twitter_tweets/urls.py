
from django.urls import path
from . import views

urlpatterns = [
    path('twitter-tweets/', views.twitter_tweet_list, name='twitter-tweets'),
]
