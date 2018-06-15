from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import owner

# Create your models here.


class Sacco(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=10, blank=True)
    office_location = models.CharField(max_length=200, blank=True)
    office_telephone = models.CharField(max_length=200, blank=True)
    office_email = models.EmailField(max_length=254, blank=True)
    logo = models.ImageField(upload_to='sacco_logo/', blank=True)
    details = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name

    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def update_sacco(sender, instance, created, **kwargs):
        if created:
            if instance.roles == 'sacco':
                Sacco.objects.create(user=instance)
            else:
                owner.models.Owner.objects.create(user=instance)


    @receiver(post_save,sender=settings.AUTH_USER_MODEL)
    def save_sacco(sender,instance,**kwargs):
        instance.sacco.save()

    def delete_sacco(self):
        self.delete()


class Super_list(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=8, unique=True)
    sacco = models.ForeignKey(Sacco, null=True)

    def __str__(self):
        return self.full_name


    def delete_supervisor(self):
        self.delete()