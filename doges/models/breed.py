from django.db import models

class Breed(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.TextField(unique=True)
	
  class Meta:
    db_table = 'doges\".\"breed'
    managed = False
    ordering = ['id']