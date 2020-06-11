from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import SignUpForm, SignInForm
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import employee_Details, per_table, cust_details, cust_pkg_details,transc_Details,consign_pkg, state_code, temp_pkg_model,t_o_delivery,consign_Details
from cargoms.forms import sender_details_form,receiver_details_form,cust_pkg_form,tr_form
from datetime import date, time
from django.db.models import Count
import datetime
import mysql.connector
import array as arr

def index(request):
    return redirect('login')

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
    det = employee_Details.objects.all()
    c_data = cust_details.objects.all()
    p_data = cust_pkg_details.objects.all()
    return render(request, 'customer_details.html', { 'c_data' : c_data, 'p_data': p_data, 'details': det })    

def expend_(request):
    det = employee_Details.objects.all()
    c_data = cust_details.objects.all()
    p_data = cust_pkg_details.objects.all()
    t_data = transc_Details.objects.all()
    v = request.POST['v']
    list = v 
    s = [str(i) for i in list] 
    res = int("".join(s)) 

    a = res
    return render(request, 'expend.html', { 'a' : a, 'c_data':c_data, 'p_data':p_data, 't_data': t_data, 'details': det })

def add_entry(request):
    det = employee_Details.objects.all()
    x = datetime.datetime.now()
    today = date.today()
    a = x.year
    b = x.month
    c = x.day
    d = 1
    c_data = cust_pkg_details.objects.all()

    for i in c_data:
        if i.pkg_r_date == today:
            d = i.s_i_no+1
        else:
            d = 1
    
    list = [a,b,c,d] 
    s = [str(i) for i in list] 
    res = int("".join(s))
    print(res)
    print("<----")
    print(today)
    h = 'Haryana'
    t_ime = datetime.datetime.now().time()
    s_form = sender_details_form(initial={'order_id': res,'s_state': h, 's_contact': 1111111111, 's_add': 'abc', 's_city': 'Faridabad'  })
    r_form = receiver_details_form(initial={'r_state': h, 'r_contact': 2222222222 , 'r_add': 'xyz' })
    p_form = cust_pkg_form(initial={'pkg_r_date' : today, 'pkg_r_time' : t_ime, 'pkg_d_date' : today, 'pkg_d_time' : t_ime })
    t_form = tr_form(initial={'t_date' : today, 't_time' : t_ime })

    return render(request, 'add_entry.html', { 's_form' : s_form, 'r_form': r_form, 'p_form': p_form, 't_form': t_form , 'details': det})

def cust_save(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        cust_name = request.POST['cust_name']
        s_contact = request.POST['s_contact']
        s_add = request.POST['s_add']
        s_city = request.POST['s_city']
        s_state = request.POST['s_state']
        s_pincode = request.POST['s_pincode']
  
        r_name = request.POST['r_name']
        r_contact = request.POST['r_contact']
        r_add = request.POST['r_add']
        r_city = request.POST['r_city']
        r_state = request.POST['r_state']
        r_pincode = request.POST['r_pincode']

        pkg_r_date = request.POST['pkg_r_date']
        pkg_r_time = request.POST['pkg_r_time']
        pkg_d_date = request.POST['pkg_d_date']
        pkg_d_time = request.POST['pkg_d_time']
        pkg_weight = request.POST['pkg_weight']
        pkg_rate_p_piece = request.POST['pkg_rate_p_piece']
        pkg_quantity = request.POST['quantity']
        ship_service_type = request.POST['ship_service_type']

        t_amt = request.POST['t_amt']
        t_date = request.POST['t_date']
        t_time = request.POST['t_time']

        c_det = cust_details(order_id=order_id, cust_name=cust_name, s_contact=s_contact, s_add=s_add, s_city=s_city,s_state=s_state, s_pincode=s_pincode, r_name=r_name, r_contact=r_contact, r_add=r_add, r_city=r_city,r_state=r_state,r_pincode=r_pincode)
        
        c_det.save()

        today = date.today()
        d=1
        p_data = cust_pkg_details.objects.all()
        for i in p_data:
            if i.pkg_r_date == today:
                d = i.s_i_no+1
            else:
                d = 1

        p_det = cust_pkg_details(order_id=order_id, cust_name=cust_name, pkg_r_date=pkg_r_date, pkg_r_time=pkg_r_time, pkg_d_date=pkg_d_date,pkg_d_time=pkg_d_time, pkg_weight=pkg_weight, pkg_ship_add=r_add, pkg_ship_city=r_city, pkg_ship_pincode= r_pincode, ship_service_type=ship_service_type,s_i_no = d, quantity=pkg_quantity, pkg_rate_p_piece=pkg_rate_p_piece)
        #Customer details
        p_det.save()

        t_det = transc_Details(order_id=order_id, cust_name=cust_name, t_amt = t_amt, t_date=t_date, t_time=t_time,quantity=pkg_quantity, pkg_rate_p_piece=pkg_rate_p_piece)
        #package Details
        t_det.save()

        temp_p_model = temp_pkg_model(order_id=order_id, cust_name=cust_name, r_state=r_state, r_city=r_city, pkg_r_date=pkg_r_date,pkg_weight=pkg_weight,pkg_quantity=pkg_quantity, pkg_rate_p_piece=pkg_rate_p_piece)
        # save to temp model
        temp_p_model.save()

        return redirect('cust_det')

def cargo_det(request):
    c_pkg = consign_pkg.objects.all()
    return render(request, 'cargo_details2.html', { 'c_pkg' : c_pkg })


def sort_data(request):
    t_data = temp_pkg_model.objects.all()
    state_data = state_code.objects.all()

    today = date.today()
    tommorow = date.today() + datetime.timedelta(days=1)
    x = datetime.datetime.now()
    today = date.today()
    a = x.year
    b = x.month
    c = x.day

    s_c = None
    #n = None
    for t_d in t_data:
        for j in state_data:    
            if (t_d.r_state.lower() == j.state.lower()):
                s_c = j.state_code
                print(s_c)

        list = ['C','P',s_c, a,b,c] 
        s = [str(i) for i in list] 
        res = "".join(s)
        
        cp = consign_pkg(c_id=res,order_id=t_d.order_id,pkg_r_date=t_d.pkg_r_date,d_sh_date=tommorow,p_id=t_d.order_id)
        
        cp.save()
    
    #t_data.delete()

    return redirect('cargo_det')

def consign_Details_save(request):
    today = date.today()
    c_d = consign_pkg.objects.all().filter(pkg_r_date=today)

    l = []
    
    for i in c_d:
        l.append(i.c_id)
    
    for c in [ele for ind, ele in enumerate(l,1) if ele not in l[ind:]]:
        count = 0
        for ele in l:
            if c == ele:
                count += 1
        print("{} {}".format(c,count))
        count = 0
     
    return redirect('cargo_det')

def trans_det(request):
    return render(render, 'transaction_details.html')

def bill_det(request):
    return render(request, 'billing_management.html')

def t_o_d(request):
    return render(request, 'time_of_delivery.html')

def enquiry_(request):
    a = cust_details.objects.all()
    b = cust_pkg_details.objects.all()
    c = transc_Details.objects.all()
    d = temp_pkg_model.objects.all()
    e = consign_pkg.objects.all()

    a.delete()
    b.delete()
    c.delete()
    d.delete()
    e.delete()

    return render(request, 'enquiry.html')