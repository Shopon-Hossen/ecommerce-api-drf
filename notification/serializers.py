from rest_framework import serializers
from .models import UserNotification


class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = ["id", "user", "message", "is_read", "created_at"]
        read_only_fields = ["id", "created_at"]
