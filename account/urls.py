# accounts/urls.py
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create-user'),
    path('verify-email/<str:token>/',
         views.VerifyEmailView.as_view(), name='verify-email'),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),

    path('update/', views.UpdateUserView.as_view(), name='update-user'),
]
