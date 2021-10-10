from django.http.response import HttpResponse
from rest_framework import viewsets
from doges.serializers import PersonSerializer
from doges.models import Person

class PersonView(viewsets.ReadOnlyModelViewSet):
  
  serializer_class = PersonSerializer
  queryset = Person.objects.all()