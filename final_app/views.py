from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from django.conf import settings
from .models import User, UserProfileInfo, Trip, Post, Gear, Food
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
            return redirect('final_app:profile')
    
    else:
        form = forms.CreateProfile()
    return render(request, 'final_app/profile_create.html', {'form': form})


@login_required(login_url='/accounts/login/')
def profile_view(request):
    user = request.user
    trips = Trip.objects.filter(user=request.user).order_by('-start_date')
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
        profile_form = forms.CreateProfile(data=request.POST, instance=request.user.profile, files=request.FILES)
        if profile_form.is_valid():
            profile_form.save()
            if 'profile_picture' in request.FILES:
                profile_form.profile_picture = request.FILES['profile_picture']
            profile_form.save()
            return redirect('final_app:profile')
        else:
            return render(request, 'final_app/profile_edit.html', {'profile_form': profile_form})
    else:
        profile_form = forms.CreateProfile(instance=request.user.profile)
        trip_form = forms.CreateTrip()

    return render(request, 'final_app/profile_edit.html', {'profile_form': profile_form, 'trip_form': trip_form})


@login_required(login_url='/accounts/login/')
def trip_detail(request, slug):
    trip = Trip.objects.get(slug=slug)

    
    post_form = forms.CreatePost()
    gear_form = forms.CreateGear()
    food_form = forms.CreateFood()
    trip_form = forms.CreateTrip()

    context = {
        'trip': trip,
        'post_form' : post_form,
        'gear_form': gear_form,
        'food_form': food_form,
        'trip_form': trip_form
        
    }

    return render(request, 'final_app/trip_detail.html', context)


@login_required(login_url='/accounts/login/')    
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    trip_form = forms.CreateTrip()

    return render(request, 'final_app/post_detail.html', {'post': post, 'trip_form': trip_form})


@login_required(login_url='/accounts/login/')
def post_create(request):
    if request.method == 'POST':
        post_form = forms.CreatePost(request.POST, request.FILES)
        trip_id = request.POST.get('trip_id')

        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.user = request.user
            instance.trip = Trip.objects.get(pk=trip_id)
            instance.save()

            trip = Trip.objects.get(pk=trip_id)
            return redirect('final_app:post_detail', slug=instance.slug)       


@login_required(login_url='/accounts/login/')
def trip_create(request):
    if request.method == 'POST':
        trip_form = forms.CreateTrip(request.POST)
        
        if trip_form.is_valid():
            instance = trip_form.save(commit=False)
            instance.user = request.user
            instance.save()
            trip = Trip.objects.get(id = instance.id)
        print(trip_form.errors)
        return redirect('final_app:trip_detail', slug =trip.slug)
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

        return redirect('final_app:trip_detail', slug=trip.slug)


@login_required(login_url='/accounts/login/')
def trips(request):
    trips_completed = Trip.objects.filter(user=request.user).filter(completed=True)
    trips_future = Trip.objects.filter(user=request.user).filter(completed=False)
    trip_form = forms.CreateTrip()

    context = {
        'trips_completed':trips_completed,
        'trips_future': trips_future,
        'trip_form': trip_form
    }

    return render (request, 'final_app/trips.html', context)


@login_required(login_url='/accounts/login/')
def post_edit(request,slug ):
    post = Post.objects.get(slug=slug)

    if request.method == "POST":
        post_edit_form = forms.CreatePost(data=request.POST, instance=post, files=request.FILES)
        if post_edit_form.is_valid():
            post_edit_form.save()
            if 'image' in request.FILES:
                post_edit_form.image = request.FILES['image']
            post_edit_form.save()
            trip_form = forms.CreateTrip()
            return redirect('final_app:post_detail', slug =post.slug)
    else:
        post_edit_form = forms.CreatePost(instance=post)
        trip_form = forms.CreateTrip()

    return render(request, 'final_app/post_edit.html', {'post_edit_form': post_edit_form, 'trip_form': trip_form})


@login_required(login_url='/accounts/login/')
def trip_edit(request,slug ):
    trip = Trip.objects.get(slug=slug)
    if request.method == "POST":
        form = forms.CreateTrip(data=request.POST, instance=trip)
        if form.is_valid():
            form.save()   
        return redirect('final_app:trip_detail', slug =trip.slug)
    else:
        form = forms.CreateTrip(instance=trip)
    return render(request, 'final_app/trip_edit.html', {'form': form})


@login_required(login_url='/accounts/login/')
def gear_create(request):
    if request.method == 'POST':
        gear_form = forms.CreateGear(request.POST)
        trip_id = request.POST.get('trip_id')
        
        if gear_form.is_valid():
            instance = gear_form.save(commit=False)
            instance.trip = Trip.objects.get(pk=trip_id)
            instance.save()

            trip = Trip.objects.get(pk=trip_id)
            return redirect('final_app:trip_detail', slug =trip.slug)
 
    return redirect('final_app:trip_detail')


@login_required(login_url='/accounts/login/')
def gear_edit(request,pk ):
    gear = Gear.objects.get(pk=pk)
    trip = Trip.objects.get(trip_gears=gear)
    if request.method == "POST":
        form = forms.CreateGear(data=request.POST, instance=gear)
        if form.is_valid():
            form.save()   
        return redirect('final_app:trip_detail', slug =trip.slug)
    else:
        form = forms.CreateGear(instance=gear)
    return render(request, 'final_app/gear_edit.html', {'form': form})


@login_required(login_url='/accounts/login/')
def gear_delete(request,pk ):
    gear = Gear.objects.get(pk=pk)
    trip = Trip.objects.get(trip_gears=gear)
    gear.delete()

    return redirect('final_app:trip_detail', slug =trip.slug)


@login_required(login_url='/accounts/login/')
def food_create(request):
    if request.method == 'POST':
        food_form = forms.CreateFood(request.POST)
        trip_id = request.POST.get('trip_id')
        
        if food_form.is_valid():
            instance = food_form.save(commit=False)
            instance.trip = Trip.objects.get(pk=trip_id)

            instance.save()

            trip = Trip.objects.get(pk=trip_id)
            return redirect('final_app:trip_detail', slug =trip.slug)


@login_required(login_url='/accounts/login/')
def food_edit(request,pk ):
    food = Food.objects.get(pk=pk)
    trip = Trip.objects.get(trip_foods=food)
    if request.method == "POST":
        form = forms.CreateFood(data=request.POST, instance=food)
        if form.is_valid():
            form.save()   
        return redirect('final_app:trip_detail', slug =trip.slug)

    else:
        form = forms.CreateFood(instance=food)
    return render(request, 'final_app/food_edit.html', {'form': form})


@login_required(login_url='/accounts/login/')
def food_delete(request,pk ):
    food = Food.objects.get(pk=pk)
    trip = Trip.objects.get(trip_foods=food)
    food.delete()
    return redirect('final_app:trip_detail', slug =trip.slug)



def other_profile(request, username):
    user = User.objects.get(username=username)
    trips = Trip.objects.filter(user=user).order_by('-start_date')
    trip_form = forms.CreateTrip()

    return render(request, 'final_app/other_profile.html', {'user': user, 'trips': trips,'trip_form': trip_form
})


def other_trip_detail(request,username, slug):
    trip = Trip.objects.get(slug=slug)   
    trip_form = forms.CreateTrip()

    context = {
        'trip': trip,
        'trip_form':trip_form
    }

    return render(request, 'final_app/other_trip_detail.html', context)


@login_required(login_url='/accounts/login/')    
def other_post_detail(request, username, slug):
    post = Post.objects.get(slug=slug)
    trip_form = forms.CreateTrip()

    return render(request, 'final_app/other_post_detail.html', {'post': post, 'trip_form': trip_form})


def search(request):        
    if request.method == 'GET':     
        trip_search =  request.GET.get('search')  
        trip_form = forms.CreateTrip()
    
        try:
            db_results = Trip.objects.filter(trail__icontains=trip_search).exclude(user=request.user)

        except Trip.DoesNotExist:
            db_results = None
        return render(request,'final_app/search.html',{'results':db_results, 'trip_form': trip_form})
    # else:
    #     return render(request,"search.html",{})

