from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from cargoms.models import cust_details,cust_pkg_details, transc_Details


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

state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))

class sender_details_form(forms.ModelForm):
    class Meta:
        model = cust_details
        fields = ('order_id', 'cust_name', 's_contact', 's_add', 's_city', 's_state', 's_pincode')
        labels = {"order_id" : "Order ID", 'cust_name' : 'Customer Name', 's_add' : 'Sender Address', 's_city' : 'Sender City', 's_state':'Sender State',  's_pincode' : 'Sender Pincode', 's_contact': 'Sender Contact'}

class receiver_details_form(forms.ModelForm):
    r_state = forms.ChoiceField(label="Reciever State", choices=state_choices)
    class Meta:
        model = cust_details
        fields = {'r_name', 'r_contact', 'r_add', 'r_city', 'r_state', 'r_pincode' }
        labels = {'r_name':'Reciever Name', 'r_contact': 'Reciever Contact', 'r_add': 'Reciever Address', 'r_city':'Reciever City', 'r_state':'Reciever State', 'r_pincode':'Reciever Pincode' }

d_type = (
    ("Normal","Normal"),
    ("Express", "Express"),
    ("Fragile", "Fragile"),
)



class cust_pkg_form(forms.ModelForm):
    ship_service_type = forms.ChoiceField(label="Service Type", choices=d_type)
    class Meta:
        model = cust_pkg_details
        fields = {'pkg_r_date','pkg_r_time','pkg_d_date', 'pkg_d_time','pkg_weight','ship_service_type'
        }
        labels = {'pkg_r_date':'Package Recieving Date','pkg_r_time':'Package Receiving Time','pkg_d_date':'Package Delivery date', 'pkg_d_time':'package Delivery Time','pkg_weight':'Package Weight','ship_service_type':'Service Type'}
        
class tr_form(forms.ModelForm):
    class Meta:
        model = transc_Details
        fields = {'t_amt', 't_date', 't_time'}
        labels = {'t_amt':'Amount','t_date':'Transaction Date', 't_time':'Transaction Time'}