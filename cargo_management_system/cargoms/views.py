from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request, "admin_login_h.html")

def cust_details(request):
    return render(request,"customer_details.html")

def trans_details(request):
    return render(request , "transaction_details.html")

def bills(request):
    return render(request , "billing.html")

def cargo(request):
    return render(request , "cargo_details.html")
