from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from datetime import date
import re  # Import the regex module
from django.core.exceptions import ValidationError

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
    error = ""
    if request.method == "POST":
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        pwd = request.POST.get('pwd')
        contact = request.POST.get('contact_number')
        em = request.POST.get('emailid')
        address = request.POST.get('address')
        userpic = request.FILES.get('profile_pic')

        # Email validation
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.match(email_pattern, em):
            error = "Please enter a valid email address."
        elif len(contact) != 10 or not contact.isdigit():
            error = "Please enter a valid 10-digit contact number."
        else:
            try:
                user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
                Donor.objects.create(user=user, contact=contact, userpic=userpic, address=address)
                error = "no"
                return redirect('donor_login')  # Redirect to the login page after successful registration
            except Exception as e:
                error = "An error occurred during registration. Please try again."

    return render(request, 'donor_reg.html', {'error': error})




def ngo_reg(request):
    error = ""
    if request.method == "POST":
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        pwd = request.POST.get('pwd')
        contact = request.POST.get('contact_number')
        em = request.POST.get('emailid')
        address = request.POST.get('address')
        about = request.POST.get('aboutme')
        categories = request.POST.getlist('categories')
        profile_pic = request.FILES.get('profile_pic')
        id_pic = request.FILES.get('id_pic')

        # Email validation
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.match(email_pattern, em):
            error = "Please enter a valid email address."
        elif len(contact) != 10 or not contact.isdigit():
            error = "Please enter a valid 10-digit contact number."
        else:
            try:
                # Create User
                user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd)
                # Create NGO (adjust based on your model)
                NGO.objects.create(user=user, contact=contact, address=address, profile_pic=profile_pic, id_pic=id_pic, about=about, categories=categories)
                error = "no"
                return redirect('ngo_login')  # Redirect to login after successful registration
            except Exception as e:
                error = "An error occurred during registration. Please try again."

    return render(request, 'ngo_reg.html', {'error': error})




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

def new_ngo(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ngo = NGO.objects.filter(status="Pending")
    return render(request,'new_ngo.html',locals())

def view_ngodetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ngo=NGO.objects.get(id=pid)
    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']
        try:
            ngo.adminremark=adminremark
            ngo.status = status
            ngo.updationdate=date.today()
            ngo.save()
            error="no"
        except:
            error="yes"
    return render(request,'view_ngodetail.html',locals())

def accepted_ngo(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ngo = NGO.objects.filter(status="Approved")
    return render(request,'accepted_ngo.html',locals()) 

def all_ngo(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    ngo = NGO.objects.all()
    return render(request,'all_ngo.html',locals())

def delete_ngo(request,pid):
    User.objects.get(id=pid).delete()
    return redirect('all_ngo')


