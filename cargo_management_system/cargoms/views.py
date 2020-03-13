from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm, SignInForm

def login(request):
     form = SignInForm()
     return render(request, 'login.html', { 'signinform' : form })

def registerUser(request):
     form = SignUpForm()
     return render(request, 'registerUser.html', { 'registrationform': form })

def home(request):
     return render(request, 'home.html')