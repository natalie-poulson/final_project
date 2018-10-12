from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from django.conf import settings
from .models import User, UserProfileInfo, Trip, Post
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def landing(request):
    login_form = AuthenticationForm()
    signup_form = UserCreationForm()
    return render(request, 'final_app/landing.html',{'login_form': login_form, 'signup_form': signup_form})

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
    trips = Trip.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'user': user,
        'trips' : trips
    }
    return render(request, 'final_app/profile.html', context)


@login_required(login_url='/accounts/login/')
def profile_edit(request):
    if request.method == "POST":
        form = forms.CreateProfile(data=request.POST, instance=request.user.profile, files=request.FILES)
        if form.is_valid():
            form.save()
            if 'profile_picture' in request.FILES:
                form.profile_picture = request.FILES['profile_picture']
            form.save()
            return redirect('final_app:profile')
    else:
        form = forms.CreateProfile(instance=request.user.profile)
    return render(request, 'final_app/profile_edit.html', {'form': form})


def trip_detail(request, pk):
    trip = Trip.objects.get(id=pk)
    return render(request, 'final_app/trip_detail.html', {'trip': trip})

    
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'final_app/post_detail.html', {'post': post})