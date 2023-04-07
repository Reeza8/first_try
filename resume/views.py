from django.shortcuts import render
from resume.forms import ContactForm
from django.http import *
from django.contrib import messages
# Create your views here.

def home(request):
     if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your contact saved succefully\nThank you for your time') 
            return HttpResponseRedirect('/resume/')
        else:
            return HttpResponse('notvalid')
        
     form=ContactForm()   
     return render(request,'resume/index.html',{'form':form})
    