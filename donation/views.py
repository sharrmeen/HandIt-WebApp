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

def ngo_login(request):
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1=NGO.objects.get(user=user)
                if user1.status != "Pending":
                    login(request,User)
                    error = "no"
                else:
                    error="not"
            except:
                error="yes"
        else:
            error = "yes"
    return render(request,'ngo_login.html',locals())

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


def ngo_reg(request):
    error=""
    if request.method == "POST":
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        pwd = request.POST['pwd']
        contact = request.POST['contact_number']
        em = request.POST['email'] 
        userpic = request.FILES['profile_pic']
        idpic = request.FILES['id_pic']
        address = request.POST['address']
        aboutme = request.POST['aboutme']

        try:
            user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            NGO.objects.create(user=user,contact=contact,userpic=userpic,idpic=idpic,address=address,aboutme=aboutme,status="Pending")
            error = "no"
        except:
            error = "yes"
    return render(request,'ngo_reg.html', locals())



def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    return render(request,'donor_home.html')


def ngo_home(request):
    if not request.user.is_authenticated:
        return redirect('ngo_login')
    return render(request,'ngo_home.html')

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')

