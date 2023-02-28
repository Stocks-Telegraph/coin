from django.urls import path
from .views import today_OHLC_list

urlpatterns = [
    path("today-ohlc/", today_OHLC_list, name="today_ohlc_list"),
]
