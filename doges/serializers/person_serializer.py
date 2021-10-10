from rest_framework import serializers
from doges.models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta:
    model = Person
    fields = ['id', 'name']
