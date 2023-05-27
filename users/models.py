from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    age = models.SmallIntegerField(null=True, blank=True, )
    job = models.CharField(max_length=500)
    first_name = models.CharField(null=True, blank=True)
    last_name = models.CharField(null=True, blank=True)

