from rest_framework import serializers
from shop.serializers import ShopSerializer
from .models import (
    Product,
    Rating,
    Comment
)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=200)

    class Meta:
        model = Product
        fields = ["id", "shop", "name", "description", "price",
                  "discount_price", "stock", "cash_on_delivery", "replacement",
                  "image", "category", "create_at", "update_at"]
        
        read_only_fields  = ["id", "create_at", "update_at"]
