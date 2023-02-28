from django.urls import path
from . import views

urlpatterns = [
    path(
        "ticker-specific-coin/", views.ticker_specific_coin, name="ticker_specific_coin"
    ),
]
