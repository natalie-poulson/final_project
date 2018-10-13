from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfileInfo(models.Model):
    name = models.CharField(max_length=40)
    current_city = models.CharField(blank=True,max_length=100)
    bio = models.CharField(blank=True, max_length=200)
    profile_picture = models.ImageField(default='profile_pictures/default.png', upload_to='profile_pictures/%Y/%m')
    created_at = models.DateField(auto_now_add =True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__ (self):
        return self.name


class Trip (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='trips') 
    trail =  models.CharField(max_length=300)
    permit = models.URLField(blank=True, null=True)
    completed = models.BooleanField(default=False) 
    created_at = models.DateField(auto_now_add =True)

    def __str__ (self):
        return self.trail


class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts') 
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, related_name='trip_posts') 
    title = models.CharField(max_length=200)
    image = models.ImageField( blank=True, default='',null=True, upload_to='post_pictures/%Y/%m')
    caption = models.CharField(blank=True, max_length=200)
    body = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add =True)
    
    def __str__ (self):
        return self.title