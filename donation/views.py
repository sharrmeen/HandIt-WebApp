from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_logins(request):
    return render(request,'all_logins.html')


def donor_login(request):
    return render(request,'donor_login.html')

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