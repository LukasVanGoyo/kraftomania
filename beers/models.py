from django.db import models
from django.contrib.auth.models import AbstractUser


class Brewery(models.Model):
    name = models.CharField(max_length=300)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
