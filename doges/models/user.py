from django.db import models
from .role import Role
from .dog import Dog

class User(models.Model):
  id = models.TextField(primary_key=True)
  name = models.TextField()
  hash = models.TextField()
  email = models.EmailField(unique=True)
  role = models.ForeignKey(
    Role,
    on_delete=models.PROTECT
  )
  dogs = models.ManyToManyField(
    Dog,
    through='Parenthood',
    symmetrical=False
  )
	
  class Meta:
    db_table = 'doges\".\"user'
    managed = False