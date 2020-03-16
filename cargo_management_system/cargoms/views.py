from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm, SignInForm
from django.contrib import auth, messages

def login_v(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
 
        else:
            messages.error(request, 'Error wrong username/password')
    form = SignInForm()
    return render(request, 'login.html', { 'signinform' : form })

def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            messages.error(request, 'User Created Successfully')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registerUser.html', {'registrationform': form})

def home(request):
     return render(request, 'home.html')