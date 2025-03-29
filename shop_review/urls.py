from django.urls import path
from .views import ShopReviewListCreateView, ShopReviewDetailView

urlpatterns = [
    path('<int:shop_id>/', ShopReviewListCreateView.as_view(), name='shop-reviews'),
    path('reviews/<int:pk>/', ShopReviewDetailView.as_view(), name='review-detail'),
]
