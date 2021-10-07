from rest_framework import serializers
from doges.models import Role

class RoleSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta:
    model = Role
    fields = ['id', 'name']
