from django.db import models

# Create your models here.
class Library(models.Model):
    name=models.CharField(max_length=15)
    author=models.CharField(max_length=15)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    yop=models.DateField()
    
