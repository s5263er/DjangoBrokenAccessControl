from django.shortcuts import render
from . import views
from . import urls
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "register/index.html")
def login(request):
    return render(request, "register/login.html")

def register(request):
    return render(request, "register/register.html")



def logout(request):
    pass