# serializers.py
from rest_framework import serializers
from .models import Comment
from account.serializers import UserMiniSerializer

class CommentSerializer(serializers.ModelSerializer):
    user_data = UserMiniSerializer(source="user", read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["id", "user", "create_at", "updated_at", "product"]
