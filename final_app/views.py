from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from django.conf import settings
from .models import User, UserProfileInfo, Trip, Post, Gear
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
        # else: 
        #     print(form.errors)
        #     return render(request, 'final_app/profile_create.html', {'form': form})
    else:
        form = forms.CreateProfile()
    return render(request, 'final_app/profile_create.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile_view(request):
    user = request.user
    trips = Trip.objects.filter(user=request.user).order_by('-created_at')
    trip_form = forms.CreateTrip()

    context = {
        'user': user,
        'trips' : trips,
        'trip_form': trip_form
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
            return render(request, 'final_app/profile_edit.html', {'form': form})
    else:
        form = forms.CreateProfile(instance=request.user.profile)
    return render(request, 'final_app/profile_edit.html', {'form': form})


def trip_detail(request, pk):
    trip = Trip.objects.get(id=pk)
    post_form = forms.CreatePost()
    gear_form = forms.CreateGear()

    context = {
        'trip': trip,
        'post_form' : post_form,
        'gear_form': gear_form
    }

    return render(request, 'final_app/trip_detail.html', context)

    
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'final_app/post_detail.html', {'post': post})


def post_create(request):
    if request.method == 'POST':
        post_form = forms.CreatePost(request.POST, request.FILES)
        trip_id = request.POST.get('trip_id')

        print("TRIP:", trip_id)
        print("USER:", request.user)
        
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.user = request.user
            instance.trip = Trip.objects.get(pk=trip_id)
            instance.save()

            trip = Trip.objects.get(pk=trip_id)
            post_form = forms.CreatePost()
            gear_form = forms.CreateGear()

            context = {
                'trip': trip,
                'post_form' : post_form,
                'gear_form': gear_form
            }

            return render(request, 'final_app/trip_detail.html', context)        
        # print(post_form.errors)
        # return render(request, 'final_app/trip_detail.html', {'post_form': post_form})
    return redirect('final_app:trip_detail')



def trip_create(request):
    if request.method == 'POST':
        trip_form = forms.CreateTrip(request.POST)
        
        if trip_form.is_valid():
            instance = trip_form.save(commit=False)
            instance.user = request.user
            instance.save()

            return redirect('final_app:profile')       
        # print(trip_form.errors)
        # return render(request, 'final_app/profile.html', {'trip_form': trip_form})
    return redirect('final_app:profile')



@login_required(login_url='/accounts/login/')
def trip_delete(request):
    if request.method == 'POST':
        trip_id = request.POST.get('trip_id')
        trip = Trip.objects.get(pk=trip_id)
        trip.delete()
        return redirect('final_app:profile')


@login_required(login_url='/accounts/login/')
def post_delete(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(pk=post_id)
        trip = Trip.objects.get(pk=post.trip.id)

        post.delete()

        post_form = forms.CreatePost()
        gear_form = forms.CreateGear()

        context = {
            'trip': trip,
            'post_form' : post_form,
            'gear_form': gear_form
        }

        return render(request, 'final_app/trip_detail.html',context )


def trips_completed(request):
    trips = Trip.objects.filter(user=request.user).filter(completed=True)

    return render (request, 'final_app/trip_list.html', {'trips': trips})


def trips_future(request):
    trips = Trip.objects.filter(user=request.user).filter(completed=False)

    return render (request, 'final_app/trip_list.html', {'trips': trips})


@login_required(login_url='/accounts/login/')
def post_edit(request,pk ):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = forms.CreatePost(data=request.POST, instance=post, files=request.FILES)
        if form.is_valid():
            form.save()
            if 'image' in request.FILES:
                form.image = request.FILES['image']
            form.save()
            return render(request, 'final_app/post_detail.html', {'post': post})
        else:
            return render(request, 'final_app/post_edit.html', {'form': form})
    else:
        form = forms.CreatePost(instance=post)
    return render(request, 'final_app/profile_edit.html', {'form': form})


@login_required(login_url='/accounts/login/')
def trip_edit(request,pk ):
    trip = Trip.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.CreateTrip(data=request.POST, instance=trip)
        if form.is_valid():
            form.save()   

            post_form = forms.CreatePost()
            gear_form = forms.CreateGear()

            context = {
                'trip': trip,
                'post_form' : post_form,
                'gear_form': gear_form
            }

            return render(request, 'final_app/trip_detail.html', context)
        # else:
        #     return render(request, 'final_app/trip_edit.html', {'form': form})
    else:
        form = forms.CreateTrip(instance=trip)
    return render(request, 'final_app/trip_edit.html', {'form': form})


def gear_create(request):
    if request.method == 'POST':
        gear_form = forms.CreateGear(request.POST)
        trip_id = request.POST.get('trip_id')
        
        if gear_form.is_valid():
            instance = gear_form.save(commit=False)
            instance.trip = Trip.objects.get(pk=trip_id)
            instance.save()

            trip = Trip.objects.get(pk=trip_id)
            post_form = forms.CreatePost()
            gear_form = forms.CreateGear()

            context = {
                'trip': trip,
                'post_form' : post_form,
                'gear_form': gear_form
            }
            return render(request, 'final_app/trip_detail.html', context)    

        # print(gear_form.errors)
        # return render(request, 'final_app/trip_detail.html', {'gear_form': gear_form})

    return redirect('final_app:trip_detail')



@login_required(login_url='/accounts/login/')
def gear_edit(request,pk ):
    gear = Gear.objects.get(pk=pk)
    trip = Trip.objects.get(trip_gears=gear)
    if request.method == "POST":
        form = forms.CreateGear(data=request.POST, instance=gear)
        if form.is_valid():
            form.save()   

            post_form = forms.CreatePost()
            gear_form = forms.CreateGear()

            context = {
                'trip': trip,
                'post_form' : post_form,
                'gear_form': gear_form
            }

            return render(request, 'final_app/trip_detail.html', context)
        # else:
        #     return render(request, 'final_app/trip_edit.html', {'form': form})
    else:
        form = forms.CreateGear(instance=gear)
    return render(request, 'final_app/gear_edit.html', {'form': form})


@login_required(login_url='/accounts/login/')
def gear_delete(request,pk ):
    gear = Gear.objects.get(pk=pk)
    trip = Trip.objects.get(trip_gears=gear)
    gear.delete()
    post_form = forms.CreatePost()
    gear_form = forms.CreateGear()
   
    context = {
        'trip': trip,
        'post_form' : post_form,
        'gear_form': gear_form
    }

    return render(request, 'final_app/trip_detail.html', context)