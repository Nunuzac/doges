from rest_framework import serializers
from doges.models import Breed

class BreedSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta:
      model = Breed
      fields = ['id', 'name']