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


class CreatePost(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ('title', 'image', 'caption', 'body')


class CreateTrip(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )     
    end_date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )   

    class Meta():
        model = models.Trip
        fields = ('trail', 'permit', 'completed', 'start_date', 'end_date')


class CreateGear(forms.ModelForm):
    class Meta():
        model = models.Gear
        fields = ('gear_name', 'packed')