from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProductFAQListCreate.as_view()),
    path('delete/<int:pk>/', views.ProductFAQDeleteView.as_view()),
]
