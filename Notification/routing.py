from django.urls import path

from . import consumer

websocket_urlpatterns = [
    path('ws/notification/<int:user_id>/', consumer.NotificationConsumer),
]
