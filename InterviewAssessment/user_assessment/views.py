from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
@login_required()
def home(request):
    return render(request,'home.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(request,username=u,password=p)
        if user:
            login(request,user)
            return redirect('user_assessment:home')
        else:
            messages.error(request, "invalid user")
    return render(request,'login.html')

def register(request):
    if(request.method=="POST"):
        u =request.POST['u']
        e = request.POST['e']
        p = request.POST['p']
        cp = request.POST['cp']
        if(p==cp):
            u=User.objects.create(username=u,password=p,email=e)
            u.save()
            return redirect('user_assessment:login')
        else:
            messages.error(request,"PASSWORDS ARE NOT SAME")

    return render(request,'register.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_assessment:login')
