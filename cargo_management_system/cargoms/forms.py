from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(label='Full Name', max_length=100 , required=True)
    employee_Id = forms.IntegerField(label='Employee ID', min_value=4, required=True)
    username = forms.CharField(label='login ID', min_length=6, max_length=10, required=True)
    email = forms.EmailField(label='E-mail', max_length=150, required=True)
    permissionId = forms.CharField( label='Permission ID', max_length=6, required=True)
    contact = forms.CharField(label='Mobile Number', max_length=10, required=True)
    address = forms.CharField(label='Address', max_length=150, required=True)
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
 
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
 
        return password2
 
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        return user

    class Meta:
        model = User
        fields = ('username', 'full_name', 'employee_Id','email', 'permissionId', 'contact', 'address')

class SignInForm(AuthenticationForm):
    username = forms.CharField( label='Login ID', max_length=100)

    class meta:
        model : User 
        feilds = ('username', 'password')          