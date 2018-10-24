from django.shortcuts import render
from main_server.views import sign_up as main_sign_up
from main_server.views import login as main_login
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from main_server.views import reset_password as main_reset_password
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        res = main_sign_up(request).content.decode()

        if res.startswith("#FAIL"):
            return render(request,'sign_up.html')
        else:
            return HttpResponse(res)
    else:
        return render(request,'sign_up.html')

def login(request):
    if request.method == 'POST':
        res = main_login(request)
        return HttpResponse(res.content.decode())
    else:
        return render(request,'login.html')



def reset_password(request):
    if request.method == 'POST':
        res = main_reset_password(request)
        return HttpResponse(res.content.decode())
    else:
        return render(request,'reset_password.html')
