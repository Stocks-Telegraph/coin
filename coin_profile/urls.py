from django.urls import path
from . import views

urlpatterns = [
    path("coin-profile/", views.coin_profile_list, name="coin-profile"),
]
