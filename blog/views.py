from django.shortcuts import render
from django.http import *
def home(request):
    return render(request,'blog/blog-home.html')
def single(request):
    return render(request,'blog/blog-single.html')