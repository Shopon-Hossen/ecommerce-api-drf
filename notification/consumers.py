from channels.generic.websocket import WebsocketConsumer
from account.models import User
from django.contrib.auth.models import AnonymousUser
import json
from asgiref.sync import async_to_sync
from .models import UserNotification


class UserNotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.user: User = self.scope["user"]
        if isinstance(self.user, AnonymousUser):
            self.close()
            return
    
        self.group_name = f"user_{self.user.id}_notification"

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()
        self.send(json.dumps({
            "status": "connection_established",
            "user": str(self.user),
            "not_read_notification_count": UserNotification.objects.filter(user=self.user, is_read=False).count()
        }))


    def disconnect(self, code):
        if isinstance(self.user, AnonymousUser):
            return
        
        if hasattr(self, "group_name") and hasattr(self, "channel_name"):
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name,
                self.channel_name
            )

    def send_notification(self, event):
        # event = {'type': 'send_notification', 'message': 'hhh'}
        self.send(json.dumps({
            "status": "new_notification",
            "notification_message": event.get("message", "No Message"),
            "not_read_notification_count": UserNotification.objects.filter(user=self.user, is_read=False).count()
        }))
