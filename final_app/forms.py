from django import forms
from django.contrib.auth.models import User
from final_app.models import UserPofileInfo

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Passord'}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')


class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Bio'}))
    
    class Meta():
        model = UserPofileInfo
        fields = ('name', 'bio', 'profile_picture')