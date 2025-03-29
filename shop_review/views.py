from rest_framework import generics, permissions
from .models import ShopReview, Shop
from .serializers import ShopReviewSerializer
from rest_framework import serializers


class ShopReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ShopReviewSerializer
    # Users must be logged in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """Retrieve all reviews for a specific shop"""
        shop_id = self.kwargs['shop_id']  # Get shop ID from URL
        return ShopReview.objects.filter(shop_id=shop_id)

    def perform_create(self, serializer):
        """Ensure a user can only review a shop they haven't reviewed before"""
        shop = Shop.objects.get(id=self.kwargs['shop_id'])

        # Prevent duplicate reviews
        if ShopReview.objects.filter(user=self.request.user, shop=shop).exists():
            raise serializers.ValidationError(
                "You have already reviewed this shop.")

        # Save review with user/shop
        serializer.save(user=self.request.user, shop=shop)


class ShopReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShopReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Ensure users can only modify their own reviews"""
        return ShopReview.objects.filter(user=self.request.user)
