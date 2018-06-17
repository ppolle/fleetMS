from django.db import models
from owner.models import Vehicle
from sacco.models import Sacco
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.


class Supervisor(models.Model):
    id_number = models.IntegerField(null=True, unique=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile_phone_number = models.IntegerField(null=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/supervisor', default='/static/img/placeholder.png')
    sacco_base = models.ForeignKey(Sacco, related_name='sacco_base',null = True)

    def __str__(self):
        return self.first_name

class Driver(models.Model):
    fullname = models.CharField(max_length=100)
    id_number = models.IntegerField(unique=True)
    profile_picture = models.ImageField(
        upload_to='profile_pictures/driver', default='/static/img/placeholder.png')

    def __str__(self):
        return self.fullname
class Conductor(models.Model):
    fullname = models.CharField(max_length = 100)
    id_number = models.CharField(max_length =100)
    profile_picture = models.ImageField(upload_to = 'profile_pictures/conductor',default='/static/img/placeholder.png')

    def __str__(self):
        return self.fullname
        
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
