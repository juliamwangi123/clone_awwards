from distutils.command import upload
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    bio=models.CharField(max_length=200, blank=True, null=True)
    contact=models.CharField(max_length=100, blank=True, null=True)
    country=models.CharField(max_length=200, blank=True, null=True)
    image=models.ImageField(default='default.png', upload_to='images')


    def __str__(self):
        return f'{self.user.username} Profile'

