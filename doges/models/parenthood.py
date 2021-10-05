from django.db import models
from .user import User
from .dog import Dog

class Parenthood(models.Model):
  user = models.ForeignKey(
    User,
    on_delete=models.PROTECT
  )
  dog = models.ForeignKey(
    Dog,
    on_delete=models.PROTECT
  )
  date = models.DateField()
	
  class Meta:
    db_table = 'doges\".\"parenthood'
    managed = False