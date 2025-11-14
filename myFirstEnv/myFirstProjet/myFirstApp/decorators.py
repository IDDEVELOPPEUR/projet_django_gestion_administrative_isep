from django.http import HttpResponse
from django.shortcuts import redirect

def authenticated(view_called):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home_connect')
        else:
            return view_called(request, *args, **kwargs)
    return wrapper
