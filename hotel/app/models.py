from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.TextField()
    marks=models.IntegerField()
    branch=models.TextField()
    age=models.IntegerField()
    address=models.TextField()


