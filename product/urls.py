from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='list-product'),
    path('create/', views.ProductCreateView.as_view(), name='create-product'),
]