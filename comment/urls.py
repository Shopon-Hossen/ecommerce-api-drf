from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CommentListCreateView.as_view()),
    path('<int:pk>/', views.CommentDetailUpdateDeleteView.as_view()),
]
