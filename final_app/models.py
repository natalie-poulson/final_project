from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.gis.db import models as gismodels
from django.contrib.gis.geos import Point


class UserProfileInfo(models.Model):
    PRIVATE = 'PRIVATE'
    PUBLIC = 'PUBLIC'
    PRIVACY_CHOICES = (
        (PRIVATE,"Private"),
        (PUBLIC,"Public")
    )
    privacy_choice = models.CharField(max_length=7,choices=PRIVACY_CHOICES, default= PUBLIC)
    name = models.CharField(max_length=40)
    current_city = models.CharField(blank=True,max_length=100)
    bio = models.CharField(blank=True, max_length=200)
    profile_picture = models.ImageField(default='../static/default.png', upload_to='profile_pictures/%Y/%m')
    created_at = models.DateField(auto_now_add =True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__ (self):
        return self.name
    

class Trip (models.Model):
    location = gismodels.PointField(blank=True, null=True, geography=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='trips') 
    slug = models.SlugField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    trail =  models.CharField(max_length=300)
    permit = models.URLField(blank=True, null=True)
    completed = models.BooleanField(default=False) 
    created_at = models.DateField(auto_now_add =True)

    def __str__ (self):
        return self.trail

    def total_days(self):
        return ((self.end_date - self.start_date).days +1)

    def day_range(self):
        return range((self.end_date - self.start_date).days+1)

    def lat(self):
        return '%s ' % (self.location.y)

    def lon(self):
        return '%s ' % (self.location.x)

    # def popupContent(self):
    #   return '<p><{}</p>'.format(
    #       self.trail)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts') 
    slug = models.SlugField(unique=True)
    trip = models.ForeignKey(Trip, on_delete = models.CASCADE, related_name='trip_posts') 
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='post_pictures/%Y/%m')
    video = models.FileField(blank=True, upload_to='post_videos/%Y/%m')
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
    day = models.IntegerField(null=True)

    def __str__ (self):
        return self.food_name


def create_post_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_post_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_post_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)



def create_trip_slug(instance, new_slug=None):
    slug = slugify(instance.trail)
    if new_slug is not None:
        slug = new_slug
    qs = Trip.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_trip_slug(instance, new_slug=new_slug)
    return slug

def pre_save_trip_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_trip_slug(instance)

pre_save.connect(pre_save_trip_receiver, sender=Trip)
