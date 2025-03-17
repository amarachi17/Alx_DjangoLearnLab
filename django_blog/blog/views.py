from profile import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.
class CumstomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def Register(request):
    if request.method == 'POST':
        form = CumstomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        else:
            messages.error(request, "Your registration failed. Please check your details entered.")
    else:
       form = CumstomUserCreationForm()

    return render(request, "blog/register.html", {"form": form})

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You are logged in now.")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        
    return render(request, "blog/login.html", {"form": form})

def Logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "blog/profile.html", {"profile": profile})
