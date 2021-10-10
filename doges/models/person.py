from doges import models


from django.db import models

class Person(models.Model):    
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        db_table = 'doges\".\"person'
        managed = False