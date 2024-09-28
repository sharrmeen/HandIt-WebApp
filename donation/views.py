from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'all_logins.html')

def all_logins(request):
    return render(request,'all_logins.html')
<<<<<<< HEAD

@login_required
def home(request):
 return render(request, "home.html", {})

def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

def donor_login(request):
    return render(request,'donor_login.html')
=======
def donor_login(request):
    return render(request,'donor_login.html')
>>>>>>> 07d92ff108e9cb27503c27e02c827294cef18bc9
