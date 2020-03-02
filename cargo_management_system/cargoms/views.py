from django.shortcuts import render
from django.contrib.auth import views as auth_views
from .forms import login

"""def login(request):
    return render(request, "base.html")"""

"""def submit(request):
    context ={}

    form = login(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    context['form']=form
    return render(request, "new.html", context)"""

def admin_login(request):
    if request.method == 'POST':
        form = login(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = login()
    return render(request, 'base.html', {'form': form})

def logged_in(request):
    return render(request, 'new.html')
 