from django import forms
from django.contrib.auth.models import User
from . import models

class CreateProfile(forms.ModelForm):
  
    class Meta():
        model = models.UserProfileInfo
        fields = ('name', 'current_city', 'bio', 'profile_picture')