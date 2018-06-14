from django.db import models

from owner.models import Vehicle
from sacco.models import Sacco

# Create your models here.


class Supervisor(models.Model):
    id_number = models.IntegerField(unique=True)
    date_of_birth = models.DateField(null=True)
    mobile_phone_number = models.CharField(max_length=13, blank=True)
    email = models.EmailField(max_length=13, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/supervisor', default='/static/img/placeholder.png')
    sacco_base = models.ForeignKey(
        Sacco, related_name='sacco_base')

    def __str__(self):
        return self.first_name


class Crew(models.Model):
    first_name = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30, unique=True)
    id_number = models.IntegerField(unique=True)
    date_of_birth = models.DateField(null=True)
    vehicle_base = models.OneToOneField(Vehicle, related_name='vehicle_base')
    profile_picture = models.ImageField(
        upload_to='profile_pictures/crew', default='/static/img/placeholder.png')

    def __str__(self):
        return self.first_name


class Issue(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    supervisor_started = models.ForeignKey(
        Supervisor, related_name='supervisor_started', null=True)

    def __str__(self):
        return self.subject


class Message(models.Model):
    message = models.TextField(max_length=4000)
    issue = models.ForeignKey(Issue, related_name='issues')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(Supervisor, related_name='posts')
    updated_by = models.ForeignKey(Supervisor, null=True, related_name='+')

    def __str__(self):
        return self.issue
