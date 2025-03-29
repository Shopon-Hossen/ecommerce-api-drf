from .models import PinnedShop
from rest_framework import serializers
from .models import Shop
from account.serializers import UserListSerializer


class ShopSerializer(serializers.ModelSerializer):
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

    def get_owner(self, obj: Shop):
        return UserListSerializer(obj.owner).data


class ShopListSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = [
            'id', 'name', 'owner', 'location', 'is_verified'
        ]
        read_only_fields = fields

    def get_owner(self, obj: Shop):
        return UserListSerializer(obj.owner).data


class PinnedShopSerializer(serializers.ModelSerializer):
    shop = serializers.SerializerMethodField()

    class Meta:
        model = PinnedShop
        fields = ["id", "user", "shop", "created_at"]
        read_only_fields = ["id", "created_at"]

    def get_shop(self, obj: PinnedShop):
        return ShopListSerializer(obj.shop).data
