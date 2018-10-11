from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from final_app.forms import RegisterForm, UserProfileInfoForm
from django.conf import settings
from .models import User, UserProfileInfo



def landing(request):
    return render(request, 'final_app/landing.html')


def register (request):
    registered = False
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user)
            return redirect('profile_create')
        else:
            print(form.errors)
    else:
        form = RegisterForm()
        context = {
            'register_form': form,
            'registered': registered
        }
        return render(request, 'final_app/register.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('profile')
            else: 
                return HttpResponse('Your account is inactive.')
        else:
            print('Login Failed')
            print(f'they used username: {username} and password: {password}')
            return HttpResponse('Invalid login details given')
    else:
        #We might need to change the path when we create this form
        return render(request, 'final_app/landing.html', {})


@login_required
def profile_create(request):
    if request.method == "POST":        
        form = UserProfileInfoForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return render(request, 'final_app/profile.html')
        else: 
            print(form.errors)
            return render(request, 'final_app/profile_create.html', {'form': form})
    else:
        form = UserProfileInfoForm()
        return render(request, 'final_app/profile_create.html', {'form': form})


@login_required
def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'final_app/profile.html', context)


@login_required
def profile_edit(request):
    user = User.objects.get(id=request.user.id)
    user, created  = UserProfileInfo.objects.get_or_create(user=user)
    user.save()

    if request.method == "POST":
        form = UserProfileInfoForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
            user.save()
            return redirect('profile')
    else:
        form = UserProfileInfoForm(instance=user)
        return render(request, 'final_app/profile_edit.html', {'form': form, 'user': user})


@login_required
def user_logout(request):
    logout(request)
    return redirect('landing')