from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfileInfo(models.Model):
    name = models.CharField(max_length=40)
    current_city = models.CharField(max_length=100, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    profile_picture = models.ImageField(default='/default.png', blank=True)
    date = models.DateTimeField(auto_now_add =True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__ (self):
        return self.name
# Create your models here.
