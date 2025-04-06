from .models import PinnedShop
from rest_framework import serializers
from .models import Shop
from account.serializers import UserMiniSerializer


class ShopMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
            'id', 'name', 'logo',
        ]
        read_only_fields = fields


class ShopSerializer(serializers.ModelSerializer):
    owner_data = UserMiniSerializer(read_only=True, source="owner")

    class Meta:
        model = Shop
        fields = [
            'id', 'name', 'owner', 'description', "owner_data",
            'logo', 'banner', 'location',
            'is_verified', 'created_at', 'updated_at'
        ]
        read_only_fields = [
            'id', 'owner',
            'is_verified', 'created_at', 'updated_at'
        ]


class PinnedShopSerializer(serializers.ModelSerializer):
    shop = serializers.SerializerMethodField()

    class Meta:
        model = PinnedShop
        fields = ["id", "user", "shop", "created_at"]
        read_only_fields = ["id", "created_at"]

    def get_shop(self, obj: PinnedShop):
        return ShopSerializer(obj.shop).data
