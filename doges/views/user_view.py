from rest_framework import viewsets
from doges.serializers import UserSerializer
from doges.models import User

class UserView(viewsets.ModelViewSet):
  
  serializer_class = UserSerializer
  queryset = User.objects.all()
