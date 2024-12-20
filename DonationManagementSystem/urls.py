"""
URL configuration for DonationManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from donation.views import *
from django.conf import settings
from django.conf.urls.static import static
from donation import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"),
    path("index.html", index, name="index_html"),
    path("all_logins",all_logins,name="all_logins"),
    path("donor_login",donor_login,name="donor_login"),
    path("ngo_login",ngo_login,name="ngo_login"),
    path("admin_login",admin_login,name="admin_login"),
    path("donor_reg",donor_reg,name="donor_reg"),
    path("ngo_reg",ngo_reg,name="ngo_reg"),
    path("donor_home",donor_home,name="donor_home"),
    path("admin_home",admin_home,name="admin_home"),
    path('ngo_home/<int:ngo_id>/', ngo_home, name='ngo_home'),
    path("new_ngo",new_ngo,name="new_ngo"),
    path("view_ngodetail/<int:pid>",view_ngodetail,name="view_ngodetail"),
    path("accepted_ngo",accepted_ngo,name="accepted_ngo"),
    path("all_ngo",all_ngo,name="all_ngo"),
    path("delete_ngo/<int:pid>",delete_ngo,name="delete_ngo"),
    path('ngos_by_category_and_city/<str:category_name>/<str:city_name>/', views.ngos_by_category_and_city, name='ngos_by_category_and_city'),
    path('ngo/<int:ngo_id>/home/', ngo_home, name='ngo_home'),
    path('donor_form/<int:ngo_id>/',donor_form, name='donor_form'),
    path("donation_history/", donation_history, name="donation_history"),
    path("donation/<int:donation_id>/", donation_detail, name="donation_detail"),
    path('test-email/', test_email, name='test_email'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset_password/<str:uid>/<str:token>/', reset_password, name='reset_password'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

