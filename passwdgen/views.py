from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
import random

# Create your views here.
def home(request):
    return render(request,'base.html')

def genpwd(request):
    if request.method=='POST':
        n=int(request.POST["no"])
        l=int(request.POST["lnth"])
        chars='abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
        password=[]
        for p in range(n):
            p=''
            for c in range(l):
                p+=(random.choice(chars))
            password.append(p)
        messages.success(request,'Passwords Generated')
        return render(request,'base.html',{'pwd':password})

    else:
        return HttpResponse('Page Not Found')

