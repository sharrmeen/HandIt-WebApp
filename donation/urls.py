from django.contrib import admin
from django.urls import path
from donation.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"),
    # path("",index,name="index"),
    path("all_logins",all_logins,name="all_logins"),
    path("donor_login",donor_login,name="donor_login"),
    path("ngo_login",ngo_login,name="ngo_login"),
    path("admin_login",admin_login,name="admin_login"),
    path("donor_reg",donor_reg,name="donor_reg"),
]