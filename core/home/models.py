from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()
    email = models.EmailField(null=True,blank= True)
    address = models.TextField(null=True,blank= True)
    image = models.ImageField()
    file = models.FileField()

class car(models.Model):
    car_name = models.CharField(max_length = 200)
    speed  = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name
    
