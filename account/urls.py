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
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),

    path('verify/', views.SendVerificationView.as_view(), name='send-verification'),
    path('verify/<str:token>/', views.ReceiveVerificationView.as_view(), name='receive-verification'),
]
