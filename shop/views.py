from account.permissions import IsVerifiedUser
from .permissions import IsShopOwner
from .serializers import ShopSerializer
from .models import Shop
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the E-Commerce API"})


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
