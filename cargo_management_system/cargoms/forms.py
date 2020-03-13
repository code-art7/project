from django import forms
from .models import admin_login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

class login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = admin_login
        fields = ['log_id','name','password']

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    permissionId = forms.CharField(max_length=6)

    class Meta:
        model = User
        fields = ('full_name', 'username',  'email', 'permissionId')

class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=100)
    Name = forms.CharField(max_length=100)

    class meta:
        model : User 
        feilds = ('name', 'username', 'password')              