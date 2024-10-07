from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from datetime import date

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
                    login(request,user)
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

    # Get the category from the request
    category_name = request.GET.get('category')

    if category_name:
        # Get the Category object matching the category_name
        try:
            category = Category.objects.get(name=category_name)
            # Filter NGOs based on the selected category
            ngos = NGO.objects.filter(category=category)
        except Category.DoesNotExist:
            ngos = NGO.objects.none()  # If the category doesn't exist, return an empty queryset
    else:
        # Show all NGOs if no category is selected
        ngos = NGO.objects.all()

    return render(request, 'donor_home.html', {'ngos': ngos, 'selected_category': category_name})


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


