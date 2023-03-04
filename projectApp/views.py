from django.shortcuts import render
from django.http import *
def home(request):
    return render(request,'projectApp/index.html')
def about(request):
    return render(request,'projectApp/about.html')
def contact(request):
    return render(request,'projectApp/contact.html')
def elements(request):
    return render(request,'projectApp/elements.html')