from django.db import models

from sacco.models import Sacco

# Create your models here.


class Supervisor(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    id_number = models.IntegerField(unique=True)
    date_of_birth = models.DateField(null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/supervisor', default='/static/img/placeholder.png')
    sacco_base = models.ForeignKey(
        Sacco, related_name='sacco_base')

    def __str__(self):
        return self.first_name
