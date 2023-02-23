from django.urls import path
from . import views

urlpatterns = [
    path(
        "ticker_specific_coin/", views.ticker_specific_coin, name="ticker_specific_coin"
    ),
]
