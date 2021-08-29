from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper 

def allowed_user(allowed_role=[]):
    def alu(view_func):
        def wrapper(request, *args, **wargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_role:
                return view_func(request, *args, **wargs)
            else:
                return redirect("books")
        return wrapper
    return alu