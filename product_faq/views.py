from rest_framework import generics
from .serializers import ProductFAQSerializers
from shop.permissions import IsShopOwner
from .models import ProductFAQ
from product.models import Product
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductFAQView(generics.ListCreateAPIView):
    permission_classes = [IsShopOwner]
    serializer_class = ProductFAQSerializers

    def get_queryset(self):
        product = get_object_or_404(Product, pk=self.request.data.get("product"))
        return ProductFAQ.objects.filter(product=product)


class ProductFAQDeleteView(APIView):
    permission_classes = [IsShopOwner]
    
    def delete(self, request, pk):
        product_faq = get_object_or_404(ProductFAQ, pk=pk, product__shop__user=request.user)
        product_faq.delete()

        return Response({"detail": "FAQ deleted successfully."}, status=204)
