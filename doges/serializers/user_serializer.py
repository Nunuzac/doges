from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from doges.models import User
class UserSerializer(serializers.HyperlinkedModelSerializer):
  
  id = serializers.IntegerField(
    validators=[
      UniqueValidator(
        queryset=User.objects.all(),
        message='user with this id already exists.'
      )
    ]
  )
  name = serializers.CharField()
  class Meta():
    model = User
    fields = ['id', 'name', 'password', 'email', 'role']
    extra_kwargs = {
      'password': {'write_only': True}
    }

  def create(self, validated_data):
    return User.objects.create_user(**validated_data)
  
  def update(self, instance, validated_data):
    instance.name = validated_data.get('name', instance.name)
    password = validated_data.get('password', None)
    if password is not None:
      instance.set_password(password)
    else:
      instance.password = password
    instance.email = validated_data.get('email', instance.email)
    instance.role = validated_data.get('role', instance.role)
    instance.save()
    return instance