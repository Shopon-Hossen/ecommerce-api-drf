# middlewares.py
from channels.middleware import BaseMiddleware
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from rest_framework_simplejwt.tokens import AccessToken
from urllib.parse import parse_qs


User = get_user_model()

class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        query_string_bytes = scope.get("query_string", b"")
        query_params = parse_qs(query_string_bytes.decode('utf-8'))
        access_token = query_params.get("access_token", [None])[0]

        scope["user"] = await self.get_user(access_token)

        return await super().__call__(scope, receive, send)
    
    @database_sync_to_async
    def get_user(self, access_token):
        if not access_token:
            return AnonymousUser()

        try:
            token = AccessToken(access_token)
            user_id = token.payload.get('user_id')

            if user_id is None:
                return AnonymousUser()

            return User.objects.get(pk=user_id)

        except Exception as e:
            return AnonymousUser()
