from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CommentSerializer
from .models import Comment
from django.shortcuts import get_object_or_404
from product.models import Product
from .permissions import IsCommentOwner


class CommentListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs.get("product")
        return Comment.objects.filter(product=product_id)
    
    def perform_create(self, serializer):
        product_id = self.kwargs.get("product")
        serializer.save(user=self.request.user, product=get_object_or_404(Product, pk=product_id))


class CommentDetailUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsCommentOwner]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
