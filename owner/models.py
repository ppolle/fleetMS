"""Summary
"""
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from sacco.models import Sacco

# Create your models here.
class Vehicle(models.Model):

    """Summary

    Attributes:
        capacity (TYPE): Description
        number_plate (TYPE): Description
    """

    number_plate = models.CharField(max_length=200)
    capacity = models.IntegerField()

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
    telephone = models.IntegerField(unique=True, null=True)
    profile_pic = models.ImageField(upload_to='ownerProfile/', blank=True)
    sacco = models.ForeignKey(Sacco)
   

    def __str__(self):
        """Summary

        Returns:
            TYPE: Description
        """
        return self.user



    def __str__(self):
        return self.user


class Vehicle(models.Model):
    number_plate = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.number_plate
