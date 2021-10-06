from rest_framework import viewsets
from doges.serializers import DogSerializer
from doges.models import Dog

class DogView(viewsets.ModelViewSet):
  
  serializer_class = DogSerializer
  queryset = Dog.objects.all()
