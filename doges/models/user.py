from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db.models.fields.related import ForeignKey
from .role import Role
from .person import Person

class UserManager(BaseUserManager):
  
  def create_user(self, id, name, email, role, password):
    user = self.model(
      id=id,
      name=name,
      email=self.normalize_email(email),
      role=role
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
class User(Person, AbstractBaseUser):
  password = models.TextField()
  email = models.EmailField(unique=True)
  role = models.ForeignKey(
    Role,
    on_delete=models.PROTECT
  )
  last_login = None

  objects = UserManager()

  USERNAME_FIELD = 'id'
  REQUIRED_FIELDS = ['name', 'password', 'email', 'role']
  class Meta:
    db_table = 'doges\".\"user'
    managed = False