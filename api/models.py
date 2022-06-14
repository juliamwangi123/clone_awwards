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
    name=models.CharField(max_length=40, blank=True, null=True)
    url=models.URLField(null=False)
    date_posted=models.DateTimeField(default=timezone.now)
    reviews=models.ManyToManyField('Review',blank=True)


    def __str__(self):
        return self.url

RATE_CHOICES =[
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
   
 ]
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Site, on_delete=models.CASCADE)
    review=models.TextField()
    review_rating=models.CharField(choices=RATE_CHOICES, max_length=130,null=True)


