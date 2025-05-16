from . import views
from django.urls import path


urlpatterns = [
    path('request-user-verify/', views.RequestUserVerifyView.as_view()),
    path('update-user/<int:pk>/', views.UpdateUser.as_view()),
]
