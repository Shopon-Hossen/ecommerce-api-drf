from django.urls import path
from . import views

urlpatterns = [
    path('list-create/', views.CartItemListCreateView.as_view(), name="list-create-cart"),
    path('delete/<int:pk>/', views.CartItemDestroyView.as_view(), name="delete-cart"),
    ]
