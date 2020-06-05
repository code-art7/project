"""cargo_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, pathk
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cargoms import views
from django.conf.urls import include,url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', views.login_v, name="login"),
    url(r'^logout/',views.logout_v, name="logout"),
    url(r'^home/', views.home, name="home"),
    url(r'^registerUser/', views.registerUser, name="registerUser"),
    url(r'^cust_det/',views.cust_det, name="cust_det"),
    url(r'^cargo_details', views.cargo_det, name="cargo_det"),
    url(r'^transactions_details', views.trans_det, name="trans_det"),
    url(r'^billing_details', views.bill_det, name="bill_det"),
    url(r'^enquiry', views.enquiry_, name="enquiry_"),
    url(r'^time_of_delivery_management', views.t_o_d, name="t_o_d"),
    url(r'^add_entry/', views.add_entry, name="add_entry"),
    url(r'^cust_save',views.cust_save, name="cust_save"),
    url(r'^expend/', views.expend_ , name="expend"),
    url(r'^sort_data', views.sort_data, name="sort_data"),
    url(r'^consign_details', views.consign_Details_save, name="c_d_s")

]
