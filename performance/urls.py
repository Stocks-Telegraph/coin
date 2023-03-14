from django.urls import path
from . import views

urlpatterns = [
    path("performance-change/", views.performance_change, name="performance_change"),
]
