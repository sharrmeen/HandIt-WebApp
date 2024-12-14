from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import date
import re 
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db import transaction  
import logging
from django.contrib.auth.models import User
from .email_utils import send_reset_email
import secrets
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib import messages
import uuid

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
    error = None
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        
        if user:
            try:
                user1 = NGO.objects.get(user=user)  # Get the NGO object for this user
                if user1.status != "Pending":
                    login(request, user)  # Log in the user
                    return redirect('ngo_home', ngo_id=user1.id)  # Redirect to NGO home
                else:
                    error = "not"  # Pending status
            except NGO.DoesNotExist:
                error = "yes"  # User not found
        else:
            error = "yes"  # Invalid credentials
    
    return render(request, 'ngo_login.html', locals())

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
                # Create a new user and donor entry
                user = User.objects.create_user(first_name=fn, last_name=ln, username=em, password=pwd, email=em)  # Save email in User model
                Donor.objects.create(user=user, contact=contact, userpic=userpic, address=address, email=em)  # Save email in Donor model
                error = "no"
                return redirect('donor_login')  # Redirect to the login page after successful registration
            except Exception as e:
                error = "An error occurred during registration. Please try again."

    return render(request, 'donor_reg.html', {'error': error})


logger = logging.getLogger(__name__)

def ngo_reg(request):
    error = ""
    categories = Category.objects.all()  # Fetch all categories
    cities = City.objects.all()

    if request.method == "POST":
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        pwd = request.POST.get('pwd')
        contact = request.POST.get('contact_number')
        em = request.POST.get('emailid')  # Capture the email address
        address = request.POST.get('address')
        about = request.POST.get('aboutme')
        selected_categories = request.POST.getlist('categories')  # Get list of selected category IDs
        profile_pic = request.FILES.get('profile_pic')
        id_pic = request.FILES.get('id_pic')
        city_id = request.POST.get('city')

        # Email validation
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        
        if not re.match(email_pattern, em):
            error = "Please enter a valid email address."
        elif len(contact) != 10 or not contact.isdigit():
            error = "Please enter a valid 10-digit contact number."
        elif not city_id:  # Validate that a city has been selected
            error = "Please select a city."
        else:
            try:
                # Ensure the following block runs as a transaction
                with transaction.atomic():
                    # Create User
                    user = User.objects.create_user(
                        first_name=fn,
                        last_name=ln,
                        username=em,  # Email used as username
                        password=pwd
                    )
                    
                    city_instance = City.objects.get(id=city_id)

                    # Create NGO object with status set to "Pending"
                    ngo = NGO.objects.create(
                        user=user,
                        contact=contact,
                        address=address,
                        email=em,  # Save the email in the NGO model
                        userpic=profile_pic,  # Correct field name
                        idpic=id_pic,  # Correct field name
                        aboutme=about,
                        city=city_instance, 
                        status='Pending'  # Explicitly set the status to "Pending"
                    )
                    
                    # Handling Many-to-Many Field (Categories)
                    category_objs = Category.objects.filter(id__in=selected_categories)  # Use category IDs
                    ngo.category.set(category_objs)  # Use set() to link selected categories
                    
                    ngo.save()  # Save the NGO object with linked categories

                error = "no"
                return redirect('ngo_login')  # Redirect to login after successful registration

            except Exception as e:
                logger.error(f"Exception during NGO registration: {e}")
                error = "An error occurred during registration. Please try again."

    return render(request, 'ngo_reg.html', {'error': error, 'categories': categories, 'cities': cities})

from django.core.mail import send_mail
from django.http import HttpResponse

def test_email(request):
    send_mail(
        'Test Subject',
        'This is a test email body.',
        'your_gmail_account@gmail.com',  # From email
        ['recipient_email@example.com'],  # To email
        fail_silently=False,
    )
    return HttpResponse("Email sent successfully")


@login_required
def donor_home(request):
    donor = Donor.objects.get(user=request.user)
    cities = City.objects.all()
    context = {
        'donor': donor,
        'donor_name': request.user.get_full_name(),  # Fetches the full name
        'email': request.user.email,  # Fetches the email directly from user, in our case username is mailid if we want to change it "change in donor_reg views"
        'cities': cities
    }
    return render(request, 'donor_home.html', context)


def ngo_home(request, ngo_id):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if the user is not authenticated

    ngo = NGO.objects.get(id=ngo_id)
    donations = Donation.objects.filter(Ngo=ngo)

    if request.method == 'POST':
        donation_id = request.POST.get('donation_id')
        status = request.POST.get('status')
        donation = Donation.objects.get(id=donation_id)
        donation.status = status
        donation.Updationdate = timezone.now()  # Update the status change date
        donation.save()

    return render(request, 'ngo_home.html', {'ngo': ngo, 'donations': donations})


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

def ngos_by_category_and_city(request, category_name, city_name):
    # Get the category by the provided name or return a 404
    category = get_object_or_404(Category, name__iexact=category_name)
    
    # Get the city by the provided name or return a 404
    city = get_object_or_404(City, name__iexact=city_name)

    # Fetch NGOs associated with the selected category and city
    ngos = NGO.objects.filter(category=category, city=city)  # Make sure your NGO model has a city field

    # Pass the selected category, city, and the list of NGOs to the template
    return render(request, 'ngos_by_category_and_city.html', {
        'ngos': ngos,
        'selected_category': category.name,
        'selected_city': city.name
    })
    

def donor_form(request, ngo_id):
    ngo = NGO.objects.get(id=ngo_id)
    if request.user.is_authenticated:
        donor = Donor.objects.get(user=request.user) 

        if request.method == 'POST':
            donor_name = request.POST.get('donor_name')
            donor_address = request.POST.get('donor_address')
            donor_phone = request.POST.get('donor_phone')
            donation_type = request.POST.get('donation_type')
            donation_photo = request.FILES.get('donation_photo')

            # # Assuming `DonationArea` is mapped to donation types like food, clothing, etc.
            # donation_area = DonationArea.objects.get(name=donation_type)

            # Create a new Donation instance and save
            donation = Donation.objects.create(
                donor=donor,
                donationname=donor_name,
                donationpic=donation_photo,
                Collectionloc=donor_address,
                Description=f"Donation of {donation_type}",
                status="Pending",  # Default status
                Donationdate=timezone.now(),
                Ngo=ngo,
                donation_type=donation_type
                # donationarea=donation_area
            )
            donation.save()

            return redirect('donor_home')

        return render(request, 'donor_form.html', {'ngo': ngo})

def donation_history(request):
    print("Donation history view accessed")
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, 'donation_history.html', {'donation': donation})

def donation_detail(request, donation_id):
    donation = get_object_or_404(Donation, id=donation_id)
    return render(request, 'donation_detail.html', {'donation': donation})

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

token_generator = PasswordResetTokenGenerator()

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(username=email)
            # Generate token and encode user ID
            token = token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri(reverse('reset_password', kwargs={'uid': uid, 'token': token}))
            subject = "Password Reset Request"
            message = render_to_string('forgot_password_email.txt', {'reset_link': reset_link})
            send_mail(subject, message, 'handit.pvt.ltd@gmail.com', [email])
            messages.success(request, "Password reset link sent to your email.")
            return redirect('forgot_password')
        except User.DoesNotExist:
            messages.error(request, "No user found with this email address.")
    return render(request, 'forgot_password.html')

def reset_password(request, uid, token):
    try:
        user_id = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=user_id)
        if token_generator.check_token(user, token):
            if request.method == 'POST':
                new_password = request.POST['new_password']
                user.set_password(new_password)
                user.save()
                messages.success(request, "Your password has been reset successfully.")
                return redirect('ngo_login')
            return render(request, 'reset_password.html', {'valid': True})
        else:
            messages.error(request, "Invalid or expired reset token.")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, "Invalid reset request.")
    return render(request, 'reset_password.html', {'valid': False})
