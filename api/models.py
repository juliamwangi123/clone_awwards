from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User)
    bio=models.CharField(max_length=200, blank=True, null=True)
    contact=models.CharField(max_length=100, blank=True, null=True)
    country=models.CharField(max_length=200, blank=True, null=True)