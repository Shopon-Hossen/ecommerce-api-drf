# accounts/views.py
from django.core.signing import BadSignature, SignatureExpired, TimestampSigner
from .models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer


signer = TimestampSigner()


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"success": True, "message": "Check you're email to verify account"})


class VerifyEmailView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, token):
        try:
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
