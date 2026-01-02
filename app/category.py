from django.db import models

#create your models here

class Category(models.Model):
    name=models.CharField(max_length=32)

    def __str__(self):
        return self.name