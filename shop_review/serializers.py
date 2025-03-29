from rest_framework import serializers
from .models import ShopReview

class ShopReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Show user name instead of ID
    shop = serializers.StringRelatedField(read_only=True)  # Show shop name instead of ID

    class Meta:
        model = ShopReview
        fields = ['id', 'user', 'shop', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'user', 'shop', 'created_at']  # Prevent editing these fields
