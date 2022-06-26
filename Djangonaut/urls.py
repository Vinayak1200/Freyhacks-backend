#Function of urls.py : Recieves requests made by user in browser,
#and decides which function to fire in views.py for creating a response
from django.contrib import admin
from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^admin/$', admin.site.urls),
    re_path(r'^About/$', views.about),
    re_path(r'^$',views.homepage),
    re_path(r'^losangeles.html$', views.LA),
    re_path(r'^goa.html$', views.Goa),
    re_path(r'^london.html$', views.london),
    re_path(r'^switzerland.html', views.swit),
    re_path(r'^bali.html$', views.bali),
    re_path(r'^machu.html$', views.machhu),
    re_path(r'^aboutus.html$', views.about),
    re_path(r'^contactus.html', views.contact),
    re_path(r'^offers.html$', views.offer),
    re_path(r'^booknow.html$', views.book),
    re_path(r'^vacationplanner.html', views.vacation),
    re_path(r'^paris.html$', views.paris),
    re_path(r'^rome.html', views.rome),
    re_path(r'^jaipur.html', views.jaipur),
    re_path(r'^dubai.html', views.dubai),
    re_path(r'^singapore.html', views.singapore),
    re_path(r'^tokyo.html$', views.tokyo),
    re_path(r'^Tahiti.html$', views.tahiti),
    re_path(r'^Varanasi.html', views.Varanasi),
    re_path(r'^Seoul.html', views.Seoul)
]
