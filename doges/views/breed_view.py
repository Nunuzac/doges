from rest_framework import viewsets
from doges.serializers import BreedSerializer
from doges.models import Breed

class BreedView(viewsets.ModelViewSet):
  
  serializer_class = BreedSerializer
  queryset = Breed.objects.all()
