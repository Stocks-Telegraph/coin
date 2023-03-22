
from django.urls import path
from .search import search_api
urlpatterns = [
    path('search/slug=<str:slug>/', search_api, name='search_api'),
    ]