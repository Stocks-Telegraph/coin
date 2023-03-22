from django.urls import path
from . import views

urlpatterns = [
    path('historical_chart/<str:symbol>/', views.historical_chart, name='historical_chart'),
    path('historical_table/<str:symbol>/', views.historical_table, name='historical_table')
]
