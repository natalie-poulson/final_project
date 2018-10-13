from django import forms
from django.contrib.auth.models import User
from . import models

class CreateProfile(forms.ModelForm):
    name = forms.CharField(label='', 
        widget=forms.TextInput( 
            attrs={
                'placeholder': 'Name',
                }
            ))
    current_city = forms.CharField(label='',
        required=False,
        widget=forms.TextInput( 
            attrs={
                'placeholder':'Current City'
                }
        ))
    bio = forms.CharField(label='',
        required=False,
        widget=forms.TextInput( 
            attrs={
                'placeholder': 'Bio'
                }
        ))
    profile_picture = forms.ImageField(label='',
        required=False,
        )


    class Meta():
        model = models.UserProfileInfo
        fields = ('name', 'current_city', 'bio', 'profile_picture')

    # def clean_name(self):
    #     name =  self.cleaned_data('name')



class CreatePost(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('title', 'image', 'caption', 'body')


class CreateTrip(forms.ModelForm):
    class Meta():
        model = models.Trip
        fields = ('trail', 'permit', 'completed')

