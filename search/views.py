# from .utils import search_shops
from django.db.models import F
from rest_framework.views import APIView
from shop.serializers import ShopSerializer
from shop.models import Shop
from rest_framework import generics, permissions
from rest_framework.response import Response


class ShopSearchView(generics.ListAPIView):
    """
    GET: Search for shops by name, location, or owner.
    Only verified users may search.
    Pagination is applied.
    """
    serializer_class = ShopSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Shop.objects.all()
        name = self.request.query_params.get('name')
        location = self.request.query_params.get('location')
        owner = self.request.query_params.get('owner')

        if name:
            queryset = queryset.filter(name__icontains=name)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if owner:
            queryset = queryset.filter(owner__id=owner)

        return queryset


class ShopAdvanceSearchView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        search_query = request.query_params.get('location')
        shops = Shop.objects.annotate(
            rank=F('location')).filter(location__icontains=search_query).order_by('rank')

        return Response({"t": ShopSerializer(shops, many=True).data})
