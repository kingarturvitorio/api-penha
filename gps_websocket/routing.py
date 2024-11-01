# gps_app/routing.py
from django.urls import path
from .consumers import GPSConsumer

websocket_urlpatterns = [
    path('ws/gps/', GPSConsumer.as_asgi()),
]
