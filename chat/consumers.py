from channels.generic.websocket import AsyncWebsocketConsumer
from account.models import User
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
import json
from .models import ChatMessage



class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def save_message(self, sender, receiver_id, message):
        receiver = User.objects.get(id=receiver_id)
        return ChatMessage.objects.create(sender=sender, receiver=receiver, message=message)

    async def connect(self):
        self.user: User | AnonymousUser = self.scope["user"]

        if self.user.is_authenticated:
            self.room_group_name = f"user_{self.user.id}_chat"
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        receiver_id = data['receiver_id']

        saved_msg = await self.save_message(self.user, receiver_id, message)

        # send to receiver
        await self.channel_layer.group_send(
            f"user_{receiver_id}_chat",
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': self.user.id
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender_id': event['sender_id'],
        }))

