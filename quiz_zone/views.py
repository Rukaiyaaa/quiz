from django.shortcuts import render

def home(request):
    return render(request, 'registration.html')

def Userlogin(request):
    return render(request, 'login.html')

def my_view(request):
    return render(request, 'base.html')