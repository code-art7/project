from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm, SignInForm
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import employee_Details, per_table, cust_details, cust_pkg_details
import datetime
from cargoms.forms import sender_details_form,receiver_details_form,cust_pkg_form

def home(request):
    det = employee_Details.objects.all()
    per_data = per_table.objects.all()
    user = User
    if request.user.is_authenticated:
        for a in det:
            if a.e_userName == request.user.username:
                n = a.e_per_id
                print(n)

                var = list(n)
                l1 = []
                for i in range(6):
                    if  int(var[i])==1:
                        d = i+1 
                        l1.append(d)
                
                print(l1)

                return render(request, 'home.html', { 'details' : det, 'per_data' : per_data, 'l1' : l1 })
    else:
        messages.error(request, 'You Must Login First!')
        return redirect('login')

def login_v(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)

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
            full_name = form.cleaned_data.get('full_name')
            e_id = form.cleaned_data.get('employee_Id')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            mobile = form.cleaned_data.get('contact')
            address = form.cleaned_data.get('address')
            
            p_1 = form.cleaned_data.get('Customer')
            p_2 = form.cleaned_data.get('Billing')
            p_3 = form.cleaned_data.get('Cargo')
            p_4 = form.cleaned_data.get('Transactions')
            p_5 = form.cleaned_data.get('Time_of_Delivery')
            p_6 = form.cleaned_data.get('Enquiry')

            if p_1 == True:
                p_1 = 1
            else:
                p_1 = 2

            #p2
            if p_2 == True:
                p_2 = 1
            else:
                p_2 = 2
            
            #p3
            if p_3 == True:
                p_3 = 1
            else:
                p_3 = 2
            
            #p4
            if p_4 == True:
                p_4 = 1
            else:
                p_4 = 2

            #p5
            if p_5 == True:
                p_5 = 1
            else:
                p_5 = 2

            #p6
            if p_6 == True:
                p_6 = 1
            else:
                p_6 = 2

            list = [p_1,p_2,p_3,p_4,p_5,p_6] 
            s = [str(i) for i in list] 
            res = int("".join(s)) 

            permissionId = res

            user_details = employee_Details(e_userName=username, e_name=full_name, e_mail=email, e_contact=mobile, e_add=address, e_per_id=permissionId,eid_no=e_id)
            user_details.save()

            messages.error(request, 'User Created Successfully')
            return render(request, 'registerUser_success.html')
    else:
        form = SignUpForm()
    return render(request, 'registerUser.html', {'registrationform': form})

def logout_v(request):
    logout(request)
    messages.error(request, 'You are Logged out! Please Login again')
    return redirect('login')

def cust_det(request):
    c_data = cust_details.objects.all()
    p_data = cust_pkg_details.objects.all()
    return render(request, 'customer_details.html', { 'c_data' : c_data, 'p_data': p_data })     

def cargo_det(request):
    return render(request, 'cargo_details.html')

def trans_det(request):
    return render(render, 'transaction_details.html')

def bill_det(request):
    return render(request, 'billing_management.html')

def t_o_d(request):
    return render(request, 'time_of_delivery.html')

def enquiry_(request):
    return render(request, 'enquiry.html')

def add_entry(request):
    s_form = sender_details_form()
    r_form = receiver_details_form()
    p_form = cust_pkg_form()
    return render(request, 'add_entry.html', { 's_form' : s_form, 'r_form': r_form, 'p_form': p_form })

def cust_save(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        cust_name = request.POST['cust_name']
        s_contact = request.POST['s_contact']
        s_add = request.POST['s_add']
        s_city = request.POST['s_city']
        s_pincode = request.POST['s_pincode']

        r_name = request.POST['r_name']
        r_contact = request.POST['r_contact']
        r_add = request.POST['r_add']
        r_city = request.POST['r_city']
        r_pincode = request.POST['r_pincode']

        pkg_r_date = request.POST['pkg_r_date']
        pkg_r_time = request.POST['pkg_r_time']
        pkg_d_date = request.POST['pkg_d_date']
        pkg_d_time = request.POST['pkg_d_time']
        pkg_weight = request.POST['pkg_weight']
        ship_service_type = request.POST['ship_service_type']

        c_det = cust_details(order_id=order_id, cust_name=cust_name, s_contact=s_contact, s_add=s_add, s_city=s_city, s_pincode=s_pincode, r_name=r_name, r_contact=r_contact, r_add=r_add, r_city=r_city,r_pincode=r_pincode)
        
        c_det.save()

        p_det = cust_pkg_details(order_id=order_id, cust_name=cust_name, pkg_r_date=pkg_r_date, pkg_r_time=pkg_r_time, pkg_d_date=pkg_d_date,pkg_d_time=pkg_d_time, pkg_weight=pkg_weight, pkg_ship_add=r_add, pkg_ship_city=r_city, pkg_ship_pincode= r_pincode, ship_service_type=ship_service_type)

        p_det.save()

        return redirect('cust_det')

def expend_(request):
    c_data = cust_details.objects.all()
    p_data = cust_pkg_details.objects.all()
    return render(request, 'expend.html', { 'c_data' : c_data, 'p_data': p_data })