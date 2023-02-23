from django.urls import path
from . import views

urlpatterns = [
    path("social-links/", views.social_links, name="social-links"),
    path("explosure-links/", views.explosure_links, name="explosure-links"),
]
