from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        login_form = AuthenticationForm()
        if signup_form.is_valid():
            user = signup_form.save()
            login(request, user)
            return redirect('final_app:profile_create')
        print(signup_form.errors)
        return render(request, 'final_app/landing.html',{'signup_form': signup_form, 'login_form': login_form} )
    else:
        return redirect('final_app:landing')

# Login In View
def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        signup_form = UserCreationForm()
        if login_form.is_valid():
            user = login_form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('final_app:profile')
        else:
            print(login_form.errors)        
            return render(request, 'final_app/landing.html',{'login_form': login_form, 'signup_form': signup_form} )
    else:
        return redirect('final_app:landing')

# Logouts
@login_required(login_url='/accounts/login/')
def logout_view(request):
    logout(request)
    return redirect('final_app:landing')
