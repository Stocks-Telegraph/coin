from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('coin_profile.urls')),
    path('api/',include('coin_twitter_tweets.urls')),
    path('api/',include('coin_links.urls')),
    path('api/',include('coin_today_ohlc.urls')),
    path('api/',include('performance.urls')),
    path('api/',include('ticker_for_specific_coin.urls')),
    path('api/',include('crypto_historical_data.urls'))
]
