from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from .forms import login

def home(request):
     form = AuthenticationForm()
     return render(request, 'login.html', { 'signinform' : form })