from django import forms
from .models import admin_login

class login(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = admin_login
        fields = ['log_id','name','password']