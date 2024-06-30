from django.http import HttpResponse
from django.shortcuts import redirect

def authandicated(view_func):
    def wrapper_function(request, *args, **kwargs):
        user1 = request.user
        if user1.is_authenticated:
            return redirect('Home') 
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_function

def allowed_users(allowed_role=[]):
    def decoraters(view_func):
        def wrapper_function(request , *args , **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_role:
                return view_func(request, *args , **kwargs)
            else:
                return HttpResponse('you are not autherized to view')
        return wrapper_function
    return decoraters

def only_Doctor(view_func):
    def wrapper_function(request , *args , **kwargs):
        group = None 
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'petiant':
            return HttpResponse('you are not a doctor')
        
        if group == 'doctor':
            return view_func(request, *args, **kwargs)
    return wrapper_function

