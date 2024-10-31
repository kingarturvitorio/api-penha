# gps_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('tracker/', views.gps_tracker, name='gps_tracker'),
]
