from django import http
from django.shortcuts import redirect, render
from . import views
from . import urls
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from . import decorator
from django.contrib.auth.models import Group

from django.contrib.auth import login as auth_login

# Create your views here.
def home(request):
    return render(request, "register/index.html")
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username,password=pass1)

        if user is not None:
            auth_login(request,user) 
            fname = user.first_name
            return render(request,"register/index.html", {'fname':fname})

        else:
            messages.error(request,"Sen kimsiiinnnnnn cikkk disarii cikkkkkkkkkk")
            return redirect('home')
    return render(request, "register/login.html")

def register(request):

    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        mygroup = Group.objects.get(name = "customer")
        mygroup.user_set.add(myuser)

        messages.success(request,"Account succesfully created.")
        return redirect('login')

    return render(request, "register/register.html")
def logout(request):
    auth_logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect("home")

@decorator.admin_only
def GetAllUsers(request):
    if request.method == "GET":
        data = list(User.objects.all())
        return render(request,'register/allusers.html', {'data':data})
    return redirect('home')

def CustomerPage(request):
    if request.method == "GET":
        return render(request, "register/customerpage.html")
