from rest_framework import serializers
from doges.models import Dog

class DogSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta:
    model = Dog
    fields = ['id', 'name', 'color', 'breed']