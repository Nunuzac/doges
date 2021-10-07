from rest_framework import viewsets
from doges.serializers import RoleSerializer
from doges.models import Role

class RoleView(viewsets.ReadOnlyModelViewSet):
  
  serializer_class = RoleSerializer
  queryset = Role.objects.all()
