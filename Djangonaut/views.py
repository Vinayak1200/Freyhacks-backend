#Here, we will create functions that will act as a 
#response to any request made  by the user
from urllib.robotparser import RequestRate
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'aboutus.html')

def LA(request):
    return render(request, 'losangeles.html')

def Goa(request):
    return render(request, 'goa.html')

def london(request):
    return render(request, 'london.html')

def swit(request):
    return render(request, 'switzerland.html')

def bali(request):
    return render(request, 'bali.html')

def machhu(request):
    return render(request, 'machhu.html')

def about(request):
    return render(request, 'aboutus.html')

def contact(request):
    return render(request, 'contactus.html')

def offer(request):
    return render(request, 'offers.html')

def book(request):
    return render(request, 'boooknow.html')

def vacation(request):
    return render(request, 'vacationplanner.html')  

def paris(request):
    return render(request, 'paris.html')

def rome(request):
    return render(request, 'rome.html')

def jaipur(request):
    return render(request, 'jaipur.html')

def dubai(request):
    return render(request, 'dubai.html')

def singapore(request):
    return render(request, 'singapore.html')

def tokyo(request):
    return render(request, 'tokyo.html')

def tahiti(request):
    return render(request, 'Tahiti.html')

def Varanasi(request):
    return render(request, 'Varanasi.html')

def Seoul(request):
    return render(request, 'Seoul.html')