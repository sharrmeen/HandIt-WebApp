from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_logins(request):
    return render(request,'all_logins.html')


def donor_login(request):
    return render(request,'donor_login.html')

def ngo_login(request):
    return render(request,'ngo_login.html')
