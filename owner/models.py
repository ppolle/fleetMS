from django.db import models

# Create your models here.
class Owner(models.Model):
   name = models.Charfield(max_length=255)
   nat_id = models.IntegerField(unique=True,default=number)
   email = models.EmailField()
   telephone = models.IntegerField(unique=True)
   vehicle_num = models.ForeignKey(Vehicle)
   profile_pic = models.ImageField(upload_to='/media')
   sacco = models.ForeignKey(Sacco)


class Vehicle(models.Model):
	number_plate = models.Charfield()
	capacity =  models.IntegerField()