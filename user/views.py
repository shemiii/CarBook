from django.shortcuts import render,redirect
from user.models import CustomUser
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



def index(request):
    return render(request,'index.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login (request,user)
            return redirect ('booking:home')
        else:
            messages.error(request,"This user is not Registerd")
    return render(request,'login.html')


def register(request):
    if (request.method == "POST"):
        f = request.POST['f']
        u = request.POST['u']
        e = request.POST['e']
        ph = request.POST['ph']
        p1 = request.POST['p1']
        p2 = request.POST['p2']
        if(p1==p2):
            r = CustomUser.objects.create_user(first_name=f,username=u,email=e,phone=ph,password=p1)
            r.save()
            return redirect ('booking:home')
    return render(request,'register.html')


def user_logout(request):
    logout(request)
    return user_login(request)
    



