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

class NGO(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(null=True, max_length=15)
    address = models.CharField(null=True, max_length=300)
    #userpic = models.FileField(null=True)
    idpic = models.FileField(null=True)
    aboutme = models.CharField(null=True, max_length=300)
    status = models.CharField(null=True, max_length=20)
    regdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(null=True, max_length=300)
    Updationdate = models.DateField(null=True)
    def __str__(self):
        return self.User.Username

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
    status = models.CharField(null=True, max_length=50)
    Donationdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(null=True, max_length=300)
    Ngo = models.ForeignKey(NGO,on_delete=models.CASCADE)
    donationarea = models.ForeignKey(DonationArea,on_delete=models.CASCADE)
    NGOremark = models.CharField(null=True, max_length=300)
    Updationdate = models.DateField(null=True)
    def __str__(self):
        return self.id

class Gallery(models.Model):
    donation = models.ForeignKey(Donation,on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    Creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
