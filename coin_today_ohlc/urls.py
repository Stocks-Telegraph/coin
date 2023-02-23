from django.urls import path
from .views import today_OHLC_list

urlpatterns = [
    path('today_ohlc/', today_OHLC_list, name='today_ohlc_list'),
]
