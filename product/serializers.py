from rest_framework import serializers
from shop.serializers import ShopListSerializer
from .models import (
    Product,
    Rating,
    Comment
)


class ProductSerializer(serializers.ModelField):
    shop = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ["id", "shop", "name", "description", "price",
                  "discount_price", "stock", "cash_on_delivery", "replacement",
                  "image", "category", "create_at", "update_at"]
        
        read_only_fields  = ["id", "create_at", "update_at"]
    
    def get_shop(self, product):
        return ShopListSerializer(product.shop).data