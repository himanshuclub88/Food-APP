from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            uname= form.cleaned_data.get('username')
            messages.success(request,f'Welcome {uname} your account is created')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form': form })

@login_required
def profilepage(request):
    return render(request,'users/profile.html')


    


#function based created from scratch
"""
def log_in(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('food:index')
        
        else:
            return HttpResponse('failed to login')
    
    return render(request,'users/login.html')


        
    
def log_out(request):
    logout(request)
    return redirect('log_in')

"""