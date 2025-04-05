from . import views
from django.urls import path


urlpatterns = [
    path('home/', views.ShopHomeView.as_view(), name='shop-home'),
    path('', views.ShopListCreateView.as_view(), name='shop-list-create'),
    path('<int:pk>/', views.ShopDetailUpdateDeleteView.as_view(), name='shop-detail-update-delete'),
    
    path("pin/", views.PinnedShopListView.as_view(), name="pinned-shop-list"),  
    path("pin/<int:shop_id>/", views.PinShopView.as_view(), name="pin-shop"),
    path("unpin/<int:shop_id>/", views.UnpinShopView.as_view(), name="unpin-shop"),
]
