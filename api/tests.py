from django.test import TestCase

# Create your tests here.
from.models import User, Site, Review


class TestModel(TestCase):
   def test_create_user(self):
    user = User.objects.create_user(username='jj', email='jj@gmail.com', password1='password', password2='password')
    user.save()
    
    self.assertEqual(str(user), 'jj')
    
   def test_create_post(self):
    user = User.objects.create_user(username='jj', email='jj@gmail.com', password1='password', password2='password')
    user.save()
    post = Site.objects.create(user=user, image='dog.jpg', 
                               name='fist post', )
    post.save()
    
    self.assertEqual(str(post), 'jj')
    
   def test_create_ratings(self):
    user = User.objects.create_user(username='jj', email='jj@gmail.com', password1='password', password2='password')
    user.save()
    post = Site.objects.create(user=user, image='dog.jpg', 
                               name='test image', )
    post.save()