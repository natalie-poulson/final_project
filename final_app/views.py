from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from django.conf import settings
from .models import User, UserProfileInfo


def landing(request):
    return render(request, 'final_app/landing.html')

@login_required(login_url='/accounts/signup/')
def profile_create(request):
    if request.method == "POST":        
        form = forms.CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return render(request, 'final_app/profile.html')
        else: 
            print(form.errors)
            return render(request, 'final_app/profile_create.html', {'form': form})
    else:
        form = forms.CreateProfile()
    return render(request, 'final_app/profile_create.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'final_app/profile.html', context)


@login_required(login_url='/accounts/login/')
def profile_edit(request):
    user = User.objects.get(id=request.user.id)
    user, created  = UserProfileInfo.objects.get_or_create(user=user)
    user.save()

    if request.method == "POST":
        form = forms.CreateProfile(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
            user.save()
            return redirect('profile')
    else:
        form = forms.CreateForm(instance=user)
    return render(request, 'final_app/profile_edit.html', {'form': form, 'user': user})



    