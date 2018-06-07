from django.db import models

# Create your models here.

class Sacco(models.Model):
    name = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=10, unique=True)
    office_location = models.CharField(max_length=200)
    office_telephone = models.CharField(max_length=200)
    office_email = models.EmailField(max_length=254)
    logo = models.ImageField(upload_to='sacco_logo/', blank=True)
    details = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Super_list(models.Model):
    full_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return self.full_name

