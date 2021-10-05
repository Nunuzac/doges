from django.db import models

class Role(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.TextField(unique=True)
	
  class Meta:
    db_table = 'doges\".\"role'
    managed = False