from rest_framework import serializers
from shop.serializers import ShopSerializer, ShopMiniSerializer
from account.serializers import UserMiniSerializer
from .models import (
    Product,
    Rating,
)


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=200)
    shop_data = ShopSerializer(read_only=True, source="shop")
    rating_data = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "shop", "shop_data", "name", "description", "price",
                  "discount_price", "stock", "cash_on_delivery", "replacement",
                  "image", "specification", "category", "create_at", "update_at",
                  "rating_data"]
        
        read_only_fields  = ["id", "create_at", "update_at", "shop_data"]

    def get_rating_data(self, obj: Product):
        rating_list = [rating.star for rating in obj.rating.all()]
        avg = (sum(rating_list) / len(rating_list)) if rating_list else 0
        return {
            "total": len(rating_list),
            "avg": avg
        }


class ProductMiniSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=200)
    shop_data = ShopMiniSerializer(read_only=True, source="shop")
    rating_data = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ["id", "shop", "shop_data", "name", "price", "rating_data",
                  "discount_price", "cash_on_delivery", "image", "category"]
        
        read_only_fields = ["shop_data"]

    def get_rating_data(self, obj: Product):
        rating_list = [rating.star for rating in obj.rating.all()]
        avg = (sum(rating_list) / len(rating_list)) if rating_list else 0
        return {
            "total": len(rating_list),
            "avg": avg
        }


class RatingSerializer(serializers.ModelSerializer):
    user_data = UserMiniSerializer(read_only=True, source="user")

    class Meta:
        model = Rating
        fields = ["id", "product", "user", "user_data", "content", "star", "create_at"]
        read_only_fields = ["id", "create_at", "user_data", "user"]
    