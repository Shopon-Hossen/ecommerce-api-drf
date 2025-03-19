# account/serializers.py
from rest_framework import serializers
from .models import User
from .utils import send_verification_email


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',
                  'password', 'display_picture')
        # User cannot change their password and email
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.is_active = False  # Disable login until email is verified
        user.save()

        send_verification_email(user)

        return user
    
    def update(self, instance, validated_data):
        # User cannot change their password and email
        if 'password' in validated_data:
            raise serializers.ValidationError("Password cannot be changed.")

        if 'email' in validated_data:
            raise serializers.ValidationError("Email cannot be changed.")
        
        return super().update(instance, validated_data)