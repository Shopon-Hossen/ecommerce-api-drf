from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ChatMessageSerializer
from .models import ChatMessage


class ChatListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatMessageSerializer

    def get_queryset(self):
        return ChatMessage.objects.filter(receiver=self.request.user)
