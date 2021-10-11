from rest_framework import viewsets
from doges.permissions import IsOwnUserData
from doges.serializers import UserSerializer
from doges.models import User

class UserView(viewsets.ModelViewSet):

  permission_classes = [IsOwnUserData]
  
  serializer_class = UserSerializer
  queryset = User.objects.all()