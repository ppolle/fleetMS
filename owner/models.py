from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Owner(models.Model):
   
   nat_id = models.IntegerField(unique=True,default=number)
   email = models.EmailField()
   user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
   telephone = models.IntegerField(unique=True)
   vehicle_num = models.ForeignKey(Vehicle)
   profile_pic = models.ImageField(upload_to='/media')
   sacco = models.ForeignKey(Sacco)

   @receiver(post_save, sender = settings.AUTH_USER_MODEL)
   def update_owner(sender,instance,created,**kwargs):
   	if created:
   		Owner.objects.create(user = instance)
   	instance.owner.save()


class Vehicle(models.Model):
	number_plate = models.Charfield()
	capacity =  models.IntegerField()