from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('coin_profile.urls')),
    path('api/',include('coin_twitter_tweets.urls')),
    path('api/',include('coin_links.urls'))
    
]
