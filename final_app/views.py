from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from final_app.forms import UserForm


def landing(request):
    return render(request, 'final_app/landing.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('landing')


def register (request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user)
            print (f'successfully logged in: {user}')
            return HttpResponse('registered')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
        context = {
            'user_form': user_form,
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
                return HttpResponse('Logged In')
            else: 
                return HttpResponse('Your account is inactive.')
        else:
            print('Login Failed')
            print(f'they used username: {username} and password: {password}')
            return HttpResponse('Invalid login details given')
    else:
        #We might need to change the path when we create this form
        return render(request, 'final_app/landing.html', {})

