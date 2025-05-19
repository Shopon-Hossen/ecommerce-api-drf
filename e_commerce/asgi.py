import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from websocket.middleware import JWTAuthMiddleware
from django.urls import path
from notification.consumers import UserNotificationConsumer
from chat.consumers import ChatConsumer
from search.consumers import SearchConsumer


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": JWTAuthMiddleware(URLRouter([
            path('ws/notification/user/', UserNotificationConsumer.as_asgi()),
            path('ws/chat/', ChatConsumer.as_asgi()),
            path('ws/search/', SearchConsumer.as_asgi()),
        ]))
    }
)
