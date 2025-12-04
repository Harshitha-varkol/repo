from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()
    salary=models.IntegerField()
    address=models.CharField(max_length=32)
