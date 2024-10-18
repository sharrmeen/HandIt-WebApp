from django.db import models
from django.contrib.auth.models import User


class Donor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('clothes', 'Clothes'),
        ('book', 'Book'),
        ('e-waste', 'E-waste'),
        ('money', 'Money'),
    ]

    name = models.CharField(max_length=50, unique=True, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.get_name_display()

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class NGO(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(null=True, max_length=10)
    address = models.CharField(null=True, max_length=300)
    userpic = models.FileField(null=True)
    idpic = models.FileField(null=True)
    aboutme = models.CharField(null=True, max_length=300)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')
    regdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(null=True, max_length=300)
    updationdate = models.DateField(null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False) 

    category = models.ManyToManyField(Category, related_name='ngos')
    
    def __str__(self):
        return self.user.username

class DonationArea(models.Model):
    Areaname = models.CharField(null=True, max_length=100)
    Description = models.CharField(null=True, max_length=300)
    Creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Areaname

class Donation(models.Model):
    donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
    donationname = models.CharField(null=True, max_length=100)
    donationpic = models.FileField(null=True)
    Collectionloc = models.CharField(null=True, max_length=300)
    Description = models.CharField(null=True, max_length=300)
    status = models.CharField(null=True, max_length=50, default="Pending")
    Donationdate = models.DateTimeField(auto_now_add=True)
    donation_type = models.CharField(max_length=50, null=True)
    adminremark = models.CharField(null=True, max_length=300)
    Ngo = models.ForeignKey(NGO,on_delete=models.CASCADE)
    # donationarea = models.ForeignKey(DonationArea,on_delete=models.CASCADE)
    NGOremark = models.CharField(null=True, max_length=300)
    Updationdate = models.DateField(null=True)
    def __str__(self):
        return f"Donation by {self.donor.user.first_name} for {self.Ngo.user.first_name} - {self.donationname} ({self.status})"

class Gallery(models.Model):
    donation = models.ForeignKey(Donation,on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    Creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
