from rest_framework import generics
from .serializers import ProductFAQSerializer
from shop.permissions import IsShopOwner
from .models import ProductFAQ
from product.models import Product
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class ProductFAQListCreate(generics.ListCreateAPIView):
    permission_classes = [IsShopOwner]
    serializer_class = ProductFAQSerializer

    def get_queryset(self):
        product_id = self.kwargs.get("product")
        return ProductFAQ.objects.filter(product=product_id)
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get("product")
        serializer.save(product=get_object_or_404(Product, pk=product_id))


class ProductFAQDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductFAQSerializer

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.kwargs.get("product"))
        return ProductFAQ.objects.filter(product=product, product__shop__user=self.request.user)
