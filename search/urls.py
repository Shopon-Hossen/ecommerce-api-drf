from . import views
from django.urls import path

urlpatterns = [
    path('shop/', views.ShopSearchView.as_view(), name='shop-search'),
    path('shop/advance/', views.ShopAdvanceSearchView.as_view(), name='advance-shop-search'),
]
