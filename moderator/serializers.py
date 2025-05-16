from .models import RequestUserVerify
from rest_framework import serializers
from account.serializers import UserMiniSerializer


class RequestUserVerifySerializer(serializers.ModelSerializer):
    user_data = UserMiniSerializer(source="user", read_only=True)

    class Meta:
        model = RequestUserVerify
        fields = ["id", "user", "user_data", "accepted", "create_at"]
        read_only_fields = fields

    def validate(self, attrs):
        user = self.context["request"].user
        if RequestUserVerify.objects.filter(user=user).exists():
            raise serializers.ValidationError("User cannot make multiple verification requests.")
        return attrs