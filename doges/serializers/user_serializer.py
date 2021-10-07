from rest_framework import serializers
from doges.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
  
  class Meta:
    model = User
    fields = ['id', 'name', 'hash', 'email', 'role', 'dogs']
    extra_kwargs = {
      'hash': {'write_only': True}
    }