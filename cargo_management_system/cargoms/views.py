from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm, SignInForm
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import employee_Details

def login_v(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            
            return render(request, 'customer_details.html')
 
        else:
            messages.error(request, 'Error wrong username/password')
    form = SignInForm()
    return render(request, 'login.html', { 'signinform' : form })

def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            e_id = form.cleaned_data.get('employee_Id')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            mobile = form.cleaned_data.get('contact')
            address = form.cleaned_data.get('address')
            permissionId = form.cleaned_data.get('permissionId')

            user_details = employee_Details(e_userName=username, e_name=full_name, e_mail=email, e_contact=mobile, e_add=address, e_per_id=permissionId,eid_no=e_id)

            user_details.save()

            messages.error(request, 'User Created Successfully')
            return render(request, 'registerUser_success.html')
    else:
        form = SignUpForm()
    return render(request, 'registerUser.html', {'registrationform': form})

def logout_v(request):
    logout(request)
    form = SignInForm()
    messages.error(request, 'You are Logged out! Please Login again')
    return render(request, 'login.html', { 'signinform' : form })
    

def home(request):
     return render(request, 'home.html')