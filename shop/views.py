from django.shortcuts import get_object_or_404
from .models import PinnedShop, Shop
from rest_framework import status
from account.permissions import IsVerifiedUser
from .permissions import IsShopOwner
from .serializers import ShopSerializer, PinnedShopSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from account.serializers import UserSerializer


class ShopHomeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        shops = request.user.shops.all()[:10]
        pinned_shops = request.user.pinned_shops.all()[:10]

        user_serializer = UserSerializer(user)
        shops_serializer = ShopSerializer(shops, many=True)
        pinned_shops_serializer = PinnedShopSerializer(pinned_shops, many=True)

        return Response({
            "message": "Welcome to the E-Commerce API",
            "user": user_serializer.data,
            "shops": shops_serializer.data,
            "pinned_shops": pinned_shops_serializer.data,
        })


class ShopListCreateView(generics.ListCreateAPIView):
    """
    GET: List all shops.
    POST: Create a new shop. Only verified users may create.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsVerifiedUser
    ]

    def perform_create(self, serializer):
        # Automatically set the owner of the shop to the current user.
        serializer.save(owner=self.request.user)


class ShopDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a shop.
    PUT/PATCH: Update a shop.
    DELETE: Delete a shop.
    Only the shop owner (who is also verified) may update or delete.
    """
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsVerifiedUser, IsShopOwner
    ]


class PinnedShopListView(generics.ListAPIView):
    """🔹 List all pinned shops for the authenticated user"""
    serializer_class = PinnedShopSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PinnedShop.objects.filter(user=self.request.user)


class PinShopView(generics.CreateAPIView):
    """🔹 Pin a shop"""
    serializer_class = PinnedShopSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        shop_id = kwargs.get("shop_id")

        shop = get_object_or_404(Shop, id=shop_id)

        # Check if the shop is already pinned
        if PinnedShop.objects.filter(user=user, shop=shop).exists():
            return Response({"message": "Shop is already pinned"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the pinned shop entry
        pinned_shop = PinnedShop.objects.create(user=user, shop=shop)
        return Response(PinnedShopSerializer(pinned_shop).data, status=status.HTTP_201_CREATED)


class UnpinShopView(generics.DestroyAPIView):
    """🔹 Unpin a shop"""
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user = request.user
        shop_id = kwargs.get("shop_id")

        try:
            pinned_shop = PinnedShop.objects.get(user=user, shop_id=shop_id)
        except PinnedShop.DoesNotExist:
            return Response({"error": "Pinned shop not found"}, status=status.HTTP_404_NOT_FOUND)

        pinned_shop.delete()
        return Response({"message": "Shop unpinned successfully"}, status=status.HTTP_204_NO_CONTENT)
