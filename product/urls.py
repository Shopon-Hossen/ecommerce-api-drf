from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProductListCreateView.as_view(), name='list-create-product'),
    path('<int:pk>/', views.ProductDetailUpdateDeleteView.as_view(), name='detail-update-delete-product'),
    path('rating/', views.RatingListCreateView.as_view(), name='create-list-rating'),
    path('<int:product>/faqs/', include("product_faq.urls")),
    path('<int:product>/comments/', include("comment.urls")),
]
