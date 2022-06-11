from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.CharField(max_length=200, blank=True, null=True)
    country=models.CharField(max_length=200, blank=True, null=True)
    image=models.ImageField(default='default.png', upload_to='images')


    def __str__(self):
        return f'{self.user.username} Profile'



class Site(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField( null=False ,upload_to='images')
    url=models.URLField(null=False)
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.url

