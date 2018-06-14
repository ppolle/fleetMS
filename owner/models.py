"""Summary
"""
from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.dispatch import receiver
from django.db.models.signals import post_save
from sacco.models import Sacco

# Create your models here.
class Owner(models.Model):

    """Summary
    
    Attributes:
        email (TYPE): Description
        nat_id (TYPE): Description
        profile_pic (TYPE): Description
        sacco (TYPE): Description
        telephone (TYPE): Description
        user (TYPE): Description
    """
    
    nat_id = models.IntegerField(unique=True, default=00000000)
    email = models.EmailField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telephone = models.CharField(unique=True, blank=True,max_length =200)
    profile_pic = models.ImageField(upload_to='ownerProfile/', blank=True)
    sacco = models.ForeignKey(Sacco)

    def __str__(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return self.user

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def update_owner(sender, instance, created, **kwargs):
        """Summary
        
        Args:
            sender (TYPE): Description
            instance (TYPE): Description
            created (TYPE): Description
            **kwargs: Description
        """
        if created:
            Owner.objects.create(user=instance)
        instance.owner.save()



class Vehicle(models.Model):

    """Summary
    
    Attributes:
        capacity (TYPE): Description
        number_plate (TYPE): Description
    """
    
    number_plate = models.CharField(max_length=200)
    capacity = models.IntegerField()
    owner = models.ForeignKey(Owner)

    def __str(self):
        """Summary
        
        Returns:
            TYPE: Description
        """
        return self.number_plate

        @classmethod
        def my_vehicles(cls):
            vehicles = cls.objects.all()
            return vehicles
    
        def delete_vehilces(self):
            self.remove()
    
        def save_vehilces(self):
            self.save()    
    
        def update_vehicle(self, id):
            pass


