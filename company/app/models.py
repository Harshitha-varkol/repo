from django.db import models

# Create your models here.
class Employeetable(models.Model):
    name=models.CharField(max_length=20)
    phone=models.PositiveBigIntegerField()
    email=models.EmailField()
    dob=models.DateField()
    role=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=8,decimal_places=2)
    doj=models.DateField()
    experience=models.IntegerField()
    address=models.TextField()

    


    