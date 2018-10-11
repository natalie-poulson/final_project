from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings


class UserPofileInfo(models.Model):
    name = models.CharField(max_length=40)
    bio = models.CharField(max_length=200, blank=True)
    profile_picture = models.ImageField(blank=True, upload_to=settings.MEDIA_ROOT, null=True, default= settings.MEDIA_ROOT+'/default_profile_picture.png')
    date = models.DateTimeField(default=datetime.now)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    def __str__ (self):
        return self.name
# Create your models here.
