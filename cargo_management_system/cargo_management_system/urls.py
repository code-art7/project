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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cargoms import views
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^admin_login_h/', views.admin_login),
    url(r'^customer_details/', views.cust_details),
    url(r'^transaction_details/',views.trans_details),
    url(r'^billing/',views.billing),
    url(r'^cargo_details/',views.cargo),
    path('cargoms/', include('django.contrib.auth.urls')),
]
