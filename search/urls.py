from . import views
from django.urls import path

urlpatterns = [
    path('shop/', views.ShopSearchView.as_view(), name='shop-search'),
    path('product/', views.ProductSearchView.as_view(), name='product-search'),
    path('product/filter/', views.ProductFilterView.as_view(), name='product-filter'),
]
