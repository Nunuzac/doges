from django.db import models
from .breed import Breed

class Dog(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.TextField()
  color = models.TextField()
  breed = models.ForeignKey(
    Breed,
    on_delete=models.PROTECT
  )
	
  class Meta:
    db_table = 'dog'
    managed = False