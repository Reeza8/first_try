from django.shortcuts import render
from django.http import *
from projectApp.forms import ContactForm,NewsLetterForm
from django.contrib import messages


#چون مقدار حجم فایل اپلودی زیر 5 مگ بود مجبور شدم فقط همین چندفایلی که تغییر دادم و بفرستم


def IndexView(request, resource):
	return render(request,'soon.html')


def home(request):
    return render(request,'projectApp/index.html')

def about(request):
    return render(request,'projectApp/about.html')

def contact(request):
    if request.method=='POST':
        
        form=ContactForm(request.POST)
        if form.is_valid:
            temp_form=form.save(commit=False)
            temp_form.name='unknown'
            temp_form.save()
            messages.success(request, 'Your contact saved succefully') 
            #form.save() 
            #  اگر این خط کد هم باشه چه فرقی میکنه تا وقتی نباشه چون من چک کردم و جفتشون یک کار میکنن انگار
           
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('notvalid')
    form=ContactForm()   
    return render(request,'projectApp/contact.html',{'form':form})

def elements(request):
    return render(request,'projectApp/elements.html')

def news_letter(request):
    
    if request.method=='POST':
        form=NewsLetterForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('notvalid')
        
    