from . import views
from django.urls import path

urlpatterns = [
    path('', views.ShopListCreateView.as_view(), name='shop-list-create'),
    path('<int:pk>/', views.ShopDetailUpdateDeleteView.as_view(), name='shop-detail-update-delete'),
]
