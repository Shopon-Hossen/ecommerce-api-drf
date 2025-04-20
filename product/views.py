from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics
from rest_framework.exceptions import PermissionDenied, ValidationError
from account.permissions import IsVerifiedUser
from .serializers import ProductSerializer, ProductMiniSerializer, RatingSerializer
from shop.models import Shop
from .permissions import IsProductOwner
from notification.models import UserNotification
from .models import (
    Product,
    Category,
    Rating
)


class ProductDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsProductOwner]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductListCreateView(generics.ListCreateAPIView):
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


class RatingListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer

    def get_queryset(self):
        product_id = self.request.data.get("product")
        if not product_id:
            return Rating.objects.all()
        
        return get_object_or_404(Product, pk=product_id).rating.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
