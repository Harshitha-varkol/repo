from django.db import models

# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=7)
    def __str__(self):
        return self.name
    
class State(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class AadharDetails(models.Model):
    Aadhar_number=models.PositiveBigIntegerField(primary_key=True)
    first_name=models.CharField(max_length=32)
    last_name=models.CharField(max_length=32)
    father_name=models.CharField(max_length=100)
    dob=models.DateField()
    phone=models.PositiveBigIntegerField()
    mail=models.EmailField()
    gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    address=models.TextField()
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to="pics")

