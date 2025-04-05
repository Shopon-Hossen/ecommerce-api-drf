from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework.exceptions import PermissionDenied, ValidationError
from account.permissions import IsVerifiedUser
from .serializers import ProductSerializer
from shop.models import Shop
from .models import (
    Product,
    Category
)


class ProductListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    permission_classes = [IsVerifiedUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # Handel Category
        category_data = self.request.data.get('category')
        if not isinstance(category_data, str):
            raise ValidationError({
                "non_string_error": "Given 'category' must be an 'String'"
            })
        
        category, created = Category.objects.get_or_create(name=category_data.capitalize())

        # Handel Shop
        user = self.request.user
        shop = get_object_or_404(Shop, pk=self.request.data.get('shop'))
        shop_list = user.shops.all()

        if shop in shop_list:
            serializer.save(shop=shop, category=category)
        else:
            raise PermissionDenied('You do not have permission to add products to others shop.')
