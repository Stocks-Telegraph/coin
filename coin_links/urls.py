from django.urls import path
from . import views

urlpatterns = [
    path("social-links/", views.social_links, name="social-links"),
    path("explorer-links/", views.explorer_links, name="explorer-links"),
]
