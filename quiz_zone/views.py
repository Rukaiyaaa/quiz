from django.shortcuts import render

def home(request):
    return render(request, 'registration.html')

def Userlogin(request):
    return render(request, 'login.html')