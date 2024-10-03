from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_logins(request):
    return render(request,'all_logins.html')


def donor_login(request):
    if request.method == 'POST':
        U = request.POST['emailid']
        p = request.POST['pwd']
        User = authenticate(username=U, password=p)
        if User:
            login(request,User)
            error = "no"
            ##return redirect('donor_home')
        else:
            error = "yes"
    return render(request,'donor_login.html',locals())

def admin_login(request):
    if request.method == 'POST':
        U = request.POST['username']
        p = request.POST['pwd']
        User = authenticate(username=U, password=p)
        
        try:
            if User.is_staff:
                login(request,User)
                error = "no"
                ##return redirect('admin_home')
            else:
                error = "yes"

        except:
            error="yes"
    return render(request,'admin_login.html',locals())

def ngo_login(request):
    return render(request,'ngo_login.html')



def donor_reg(request):
    error=""
    if request.method == "POST":
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        pwd = request.POST['pwd']
        contact = request.POST['contact_number']
        em = request.POST['email']
        address = request.POST['address']
        userpic = request.FILES['profile_pic']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            Donor.objects.create(user=user,contact=contact,userpic=userpic,address=address)
            error = "no"
        except:
            error = "yes"
    return render(request,'donor_reg.html', locals())

def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request,'donor_home.html')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

