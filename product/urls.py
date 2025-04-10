from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='list-create-product'),
    path('<int:pk>/', views.ProductDetailUpdateDeleteView.as_view(), name='detail-update-delete-product'),
    path('rating/', views.RatingListCreateView.as_view(), name='create-list-rating'),
]
