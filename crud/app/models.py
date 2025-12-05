from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=32)
    branch=models.CharField(max_length=32)
    age=models.IntegerField()
    marks=models.IntegerField()
    address=models.CharField(max_length=32)
    