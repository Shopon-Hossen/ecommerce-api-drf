# serializers.py
from rest_framework import serializers
from .models import Cart, CartItem
from product.serializers import ProductMiniSerializer



class CartItemSerializer(serializers.ModelSerializer):
    product_data = ProductMiniSerializer(source="product", read_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "cart", "product", "quantity", "product_data"]
        read_only_fields = ["product_data", "cart", "id"]
