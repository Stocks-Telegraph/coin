from django.urls import path
from . import views

urlpatterns = [
    path(
        "ticker-for-specific-coin/", views.data_of_crypto, name="ticker_specific_coin",
    ),
    # path('create-ticker/', views.create_ticker, name='create_ticker'),
]
