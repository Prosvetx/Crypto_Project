from django.urls import path
from .consamers import CoinsConsumer



ws_urlpatterns = [
    path('ws/coins/', CoinsConsumer.as_asgi())

    ]