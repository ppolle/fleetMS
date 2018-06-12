from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from sacco.models import Sacco

# Create your models here.


class Owner(models.Model):

    nat_id = models.IntegerField(unique=True, default=00000000)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    telephone = models.IntegerField(unique=True, null=True)
    profile_pic = models.ImageField(upload_to='ownerProfile/', blank=True)
    sacco = models.ForeignKey(Sacco, null=True)

    def __str__(self):
        return self.user


class Vehicle(models.Model):
    number_plate = models.CharField(max_length=200)
    capacity = models.IntegerField()

    def __str__(self):
        return self.number_plate
