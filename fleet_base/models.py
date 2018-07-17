from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    '''
    This function will create an abstract user to create an extra field in the user model
    '''
    roles = models.TextField(max_length=100)
