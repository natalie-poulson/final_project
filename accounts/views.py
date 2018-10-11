from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Sign Up View
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('final_app:profile_create')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form': form})

# Login In View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('final_app:landing')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html', {'form': form})

# Logouts
@login_required(login_url='/accounts/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('final_app:landing')
