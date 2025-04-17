from rest_framework.permissions import IsAuthenticated
from .models import CartItem
from .serializers import CartItemSerializer
from rest_framework import generics
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError


class CartItemListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.request.user.cart)

    def perform_create(self, serializer):
        try:
            serializer.save(cart=self.request.user.cart)
        except IntegrityError:
            raise ValidationError({"error": "This product is already in your cart."})


class CartItemDestroyUpdateView(generics.DestroyAPIView, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.request.user.cart)
