# accounts/views.py
from django.shortcuts import get_object_or_404
from django.core.signing import BadSignature, SignatureExpired, TimestampSigner
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer


signer = TimestampSigner()


class UpdateUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Get the current user's details."""
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        """Update the current user's profile (excluding password)."""
        serializer = UserSerializer(
            request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Create a new user with is_active=False"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"success": True, "message": "Check you're email to verify account"})


class VerifyEmailView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, token):
        try:
            """Verify email address for user"""
            # decode the user id/pk.
            user_pk = signer.unsign(token, max_age=3600)
            user = User.objects.get(pk=user_pk)
            user.is_active = True  # Activate the user
            user.save()
            return Response({"success": True, "message": "Email verified successfully. You can now log in."}, status=201)

        except SignatureExpired:
            return Response({"message": "Verification link has expired."}, status=400)
        except BadSignature:
            return Response({"message": "Invalid verification token."}, status=400)
        except User.DoesNotExist:
            return Response({"message": "User not found."}, status=400)


class UserProfileView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        """Get a specific user's details"""
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PasswordChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        """Change the current user's password"""
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        user = request.user

        if not user.check_password(old_password):
            return Response({"error": "Old password is incorrect."}, status=400)

        user.set_password(new_password)
        user.save()
        return Response({"success": True, "message": "Password changed successfully."}, status=200)
