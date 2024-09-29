from django.contrib import admin
from django.urls import path
from donation.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"),
    path("all_logins",all_logins,name="all_logins"),
    path("donor_login",donor_login,name="donor_login"),
    
]
