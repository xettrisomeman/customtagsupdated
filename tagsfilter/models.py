from django.db import models

# Create your models here.
class Name(models.Model):
    name = models.CharField(max_length=50)
    last_name= models.CharField( max_length=50)
    age = models.IntegerField()


    def __str__(self):
        return self.name 


    