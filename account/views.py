# accounts/views.py
from .utils import send_verification_email
from django.shortcuts import get_object_or_404
from django.core.signing import BadSignature, SignatureExpired, TimestampSigner
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer


signer = TimestampSigner()


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Create a new user with is_active=False"""
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"success": True, "message": "Check you're email to verify account"})


class UpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """Get the current user's details."""
        serializer = UserSerializer(request.user)
        return Response({"success": True, "data": serializer.data})

    def patch(self, request):
        """Update the current user's profile (excluding password)."""
        serializer = UserSerializer(
            request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True, "data": serializer.data})


class VerifyEmailView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, token):
        try:
            """Verify email address for user"""
            # decode the user id/pk.
            new_password = request.data.get('new_password')
            user_pk = signer.unsign(token, max_age=3600)
            user = User.objects.get(pk=user_pk)
            response_message = "Nothing was changed"

            if not new_password:
                user.is_active = True # Activate the user
                response_message = "Account activated successfully. now you can login."

            elif new_password and user.is_active:
                user.set_password(new_password) # Set the new password
                response_message = "Password changed successfully. now you can login with new password."


            user.save()
            return Response({"success": True, "message": "Email verified successfully", "response_message": response_message}, status=201)

        except SignatureExpired:
            return Response({"message": "Verification link has expired."}, status=400)
        except BadSignature:
            return Response({"message": "Invalid verification token."}, status=400)
        except User.DoesNotExist:
            return Response({"message": "User not found."}, status=400)


class ProfileView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        """Get a specific user's details"""
        user = get_object_or_404(User, id=pk)
        serializer = UserSerializer(user)
        return Response({"success": True, "data": serializer.data})


class PasswordUpdateView(APIView):
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


class PasswordResetView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        """Reset the password for a user"""
        email = request.data.get('email')
        user = get_object_or_404(User, email=email)

        send_verification_email(user)

        return Response({"success": True, "message": "Check your email to reset your password."}, status=200)
