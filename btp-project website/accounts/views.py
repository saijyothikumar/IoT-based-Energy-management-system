

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def signup(request):
    if request.method=='POST':
        if request.POST['username'] and request.POST['password1'] and request.POST['password2']:
            if request.POST['password1']==request.POST['password2']:

                try:
                    user=User.objects.get(username=request.POST['username'])
                    return render(request,'accounts/signup.html',{'error':'username exsists'})
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                    auth.login(request,user)
                    return redirect('home')
            else:
                return render(request,'accounts/signup.html',{'error':'password didnt match'})
        else:
            return render(request,'accounts/signup.html',{'error':'all fields are required'})

    else:
        return render(request,'accounts/signup.html')

def login(request):
    if request.method=='POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST.get('password'))
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password doesnot exist'})

    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('index')
