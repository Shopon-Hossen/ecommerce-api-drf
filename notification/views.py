from rest_framework import generics, permissions
from .serializers import UserNotificationSerializer
from .models import UserNotification
from rest_framework.views import APIView
from rest_framework.response import Response


class UserNotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserNotificationSerializer

    def get_queryset(self):
        return UserNotification.objects.filter(user=self.request.user).order_by("is_read", "-created_at")


class MarkIsReadUserNotificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        requested_notification_ids = request.data.get("notification_ids", [])
        user_notifications = UserNotification.objects.filter(user=request.user)

        if "__all__" in requested_notification_ids:
            user_notifications.update(is_read=True)
            return Response({
                "status": "mark_as_read_all"
            })

        user_notifications.filter(id__in=requested_notification_ids).update(is_read=True)

        return Response({
            "status": "mark_as_read",
            "notification_ids": requested_notification_ids
        })
