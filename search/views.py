from .utils import search
from rest_framework.views import APIView
from shop.serializers import ShopMiniSerializer
from rest_framework import permissions, generics
from rest_framework.response import Response
from product.serializers import ProductMiniSerializer
from shop.models import Shop
from product.models import Product
from rest_framework.pagination import PageNumberPagination


class BaseSearch(APIView):
    permission_classes = [permissions.AllowAny]
    custom_serializer_class = None
    pagination_class = PageNumberPagination 

    def get(self, request):
        query = request.query_params.get("q")
        if not query:
            return Response({"error": "Query parameter 'q' is required."}, status=400)

        objs = self.custom_search_result(query)

        # Paginate the result
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(objs, request, view=self)
        serializer = self.custom_serializer_class(page, many=True)

        return paginator.get_paginated_response(serializer.data)

    def custom_search_result(self, query):
        return []


class ShopSearchView(BaseSearch):
    custom_serializer_class = ShopMiniSerializer

    def custom_search_result(self, query):
        return search(query, Shop, "name")


class ProductSearchView(BaseSearch):
    custom_serializer_class = ProductMiniSerializer

    def custom_search_result(self, query):
        return search(query, Product, "name")


class ProductFilterView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductMiniSerializer

    def get_queryset(self):
        q = self.request.query_params
        queryset = Product.objects.all()

        # Filter by category
        category = q.get("category")
        if category:
            queryset = queryset.filter(category__name__icontains=category)

        # Filter by price range
        min_price, max_price = q.get("min"), q.get("max")
        if min_price and max_price:
            try:
                queryset = queryset.filter(price__range=(min_price, max_price))
            except ValueError:
                pass # Just skip price filter if invalid

        # Ordering (safe list only)
        ordering = q.get("ordering")
        allowed_ordering = ["price", "-price", "rating", "-rating", "create_at", "-create_at", "replacement", "-replacement"]
        if ordering in allowed_ordering:
            queryset = queryset.order_by(ordering)

        return queryset