"""
Summary

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


class Owner(models.Model):


    nat_id = models.IntegerField(unique=True, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telephone = models.IntegerField(unique=True, null=True)
    profile_pic = models.ImageField(upload_to='ownerProfile/', blank=True)
    sacco = models.ForeignKey(Sacco, null=True)



    def __str__(self):
        """Summary

        Returns:
            TYPE: Description
        """
        return self.user


class Vehicle(models.Model):

    """Summary

    Attributes:
        capacity (TYPE): Description
        number_plate (TYPE): Description
    """

    number_plate = models.CharField(max_length=200, null=True)
    capacity = models.IntegerField(null=True)
    owner = models.ForeignKey(Owner, null=True)
    sacco = models.ForeignKey(Sacco, null=True)
    is_active = models.BooleanField(default = False)
    def __str__(self):
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
