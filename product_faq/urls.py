from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProductFAQView.as_view(), name='product-faq'),
    path('delete/<int:pk>/', views.ProductFAQDeleteView.as_view(), name='delete-product-faq'),
]
