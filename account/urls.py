from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/silent/', TokenRefreshView.as_view(), name='login-silent'),
    path('update/', views.UpdateView.as_view(), name='update'),
    path('update/password/', views.PasswordUpdateView.as_view(), name='update-password'),
    path('reset/password/', views.PasswordResetView.as_view(), name='reset-password'),

    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('email/verify/<str:token>/', views.VerifyEmailView.as_view(), name='email-verify'),
]
