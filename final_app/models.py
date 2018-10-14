from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime


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
    start_date = models.DateField()
    end_date = models.DateField()
    trail =  models.CharField(max_length=300)
    permit = models.URLField(blank=True, null=True)
    completed = models.BooleanField(default=False) 
    location = models.CharField(blank=True, max_length=400)
    lat = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=6)
    lng = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=6)
    created_at = models.DateField(auto_now_add =True)

    def __str__ (self):
        return self.trail

    def total_days(self):
        return (self.end_date - self.start_date).days


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


class Gear(models.Model):
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, related_name='trip_gears')
    gear_name = models.CharField(max_length=200)
    packed =  models.BooleanField(default=False) 

    def __str__ (self):
        return self.gear_name


class Food(models.Model):
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, related_name='trip_foods')
    food_name = models.CharField(max_length=200)
    packed =  models.BooleanField(default=False) 

    def __str__ (self):
        return self.food_name