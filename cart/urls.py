from django.urls import path
from . import views

urlpatterns = [
    path('list-create/', views.CartItemListCreateView.as_view(), name="list-create-cart"),
    path('delete-update/<int:pk>/', views.CartItemDestroyUpdateView.as_view(), name="delete-update-cart"),
]
