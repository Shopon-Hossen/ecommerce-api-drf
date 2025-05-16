from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .permissions import IsModerator
from .serializers import RequestUserVerifySerializer
from .models import RequestUserVerify
from account.models import User
from account.serializers import UserSerializer


class RequestUserVerifyView(ListCreateAPIView):
    serializer_class = RequestUserVerifySerializer
    queryset = RequestUserVerify.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsModerator()]
        return [IsAuthenticated()]
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    

class UpdateUser(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsModerator]
    
    def get_queryset(self):
        return User.objects.filter(is_staff=False, is_superuser=False)
