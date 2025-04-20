from django.urls import path
from . import consumers


ws_urlpatterns = [
    path('ws/notifications/user/', consumers.UserNotificationConsumer.as_asgi()),
]
