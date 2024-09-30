from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')

def all_logins(request):
    return render(request,'all_logins.html')

def donor_login(request):
    return render(request,'donor_login.html')
