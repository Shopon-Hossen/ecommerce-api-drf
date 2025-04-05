from .models import PinnedShop
from rest_framework import serializers
from .models import Shop


class ShopSerializer(serializers.ModelSerializer):
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


class PinnedShopSerializer(serializers.ModelSerializer):
    shop = serializers.SerializerMethodField()

    class Meta:
        model = PinnedShop
        fields = ["id", "user", "shop", "created_at"]
        read_only_fields = ["id", "created_at"]

    def get_shop(self, obj: PinnedShop):
        return ShopSerializer(obj.shop).data
