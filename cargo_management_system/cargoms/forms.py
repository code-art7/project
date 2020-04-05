from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cargoms.models import cust_details,cust_pkg_details

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(label='Full Name', max_length=100 , required=True)
    employee_Id = forms.IntegerField(label='Employee ID', min_value=4, required=True)
    username = forms.CharField(label='login ID', min_length=6, max_length=10, required=True)
    email = forms.EmailField(label='E-mail', max_length=150, required=True)
    #permissions
    Customer = forms.BooleanField(label="Customer Details", help_text="Select for provide Access to Customer Details ", required=False)
    Cargo = forms.BooleanField(label="Cargo Details", help_text="Select for provide Access to Cargo Details ", required=False)
    Transactions = forms.BooleanField(label="Transations Details", help_text="Select for provide Access to Transactions Details ", required=False)
    Time_of_Delivery = forms.BooleanField(label="Time of Delivery Details", help_text="Select for provide Access to Time of Delivery Details ", required=False) 
    Billing = forms.BooleanField(label="Billing Details", help_text="Select for provide Access to Billing Details ",required=False)
    Enquiry = forms.BooleanField(label="Enquiry", help_text="Select for provide Access to Enquiry management ", required=False)

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
        fields = ('username', 'full_name', 'employee_Id', 'Customer',  'Cargo','Transactions','Time_of_Delivery', 'Billing',   'Enquiry','email', 'contact', 'address')

class SignInForm(AuthenticationForm):
    username = forms.CharField( label='Login ID', max_length=100)

    class meta:
        model : User 
        feilds = ('username', 'password')          

class sender_details_form(forms.ModelForm):
    class Meta:
        model = cust_details
        fields = ('order_id', 'cust_name', 's_contact', 's_add', 's_city', 's_pincode')
        labels = {"order_id" : "Order ID", 'cust_name' : 'Customer Name', 's_add' : 'Sender Address', 's_city' : 'Sender City', 's_pincode' : 'Sender Pincode', 's_contact': 'Sender Contact'}

class receiver_details_form(forms.ModelForm):
    class Meta:
        model = cust_details
        fields = {'r_name', 'r_contact', 'r_add', 'r_city', 'r_pincode' }
        labels = {'r_name':'Reciever Name', 'r_contact': 'Reciever Contact', 'r_add': 'Reciever Address', 'r_city':'Reciever City', 'r_pincode':'Reciever Pincode' }

class cust_pkg_form(forms.ModelForm):
    class Meta:
        model = cust_pkg_details
        fields = {'pkg_r_date','pkg_r_time','pkg_d_date', 'pkg_d_time','pkg_weight','ship_service_type'
        }
        labels = {'pkg_r_date':'Package Recieving Date','pkg_r_time':'Package Receiving Time','pkg_d_date':'Package Delivery date', 'pkg_d_time':'package Delivery Time','pkg_weight':'Package Weight','ship_service_type':'Service Type'}
        