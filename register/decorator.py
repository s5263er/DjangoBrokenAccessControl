from django.http import HttpResponse
from django.shortcuts import redirect

def admin_only(view_func):
    def wrapper_func(request, *args ,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'customer':
            return HttpResponse('You are not authorized to access this page')
        elif group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to access this page')
    return wrapper_func