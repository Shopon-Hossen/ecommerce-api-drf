from rest_framework import serializers
from .models import Shop
from account.serializers import UserSerializer


class ShopSerializer(serializers.ModelSerializer):
    # Expose the owner’s email as a read-only field.
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = [
            'id', 'name', 'owner', 'description',
            'logo', 'banner', 'location',
            'is_verified', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'owner',
            'is_verified', 'created_at', 'updated_at'
        ]

    def get_owner(self, obj):
        return UserSerializer(obj.owner).data
