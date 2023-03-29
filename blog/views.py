from django.shortcuts import render,get_object_or_404
from django.http import *
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import *
import pytz



def home(request,**kwargs):
    #check the published date and add it if its pass
    posts=Post.objects.all()
    tz_tehran = pytz.timezone('Asia/Tehran') 
    datetime_Karachi = datetime.now(tz_tehran)
    for post in posts:
        if(post.published_date<datetime_Karachi):
            post.status=1
            post.save()

    
    posts=Post.objects.filter(status=1)
    if kwargs.get('catname')!=None:
        posts=posts.filter(category__name=kwargs['catname'])
    if kwargs.get('author')!=None:
        posts=posts.filter(author__username=kwargs['author']) 
    posts=Paginator(posts,3)
    page_number=request.GET.get('page')
    try:
        posts=posts.get_page(page_number)
    except EmptyPage:
        posts=posts.get_page(1)     
    except PageNotAnInteger:
        posts=posts.get_page(posts.num_pages)     
    content={'posts':posts}
    return render(request,'blog/blog-home.html',content)


def single2(request,pid):
    posts=get_object_or_404(Post,pk=pid,status=1)
    posts.counted_views+=1
    posts.save()
    list=Post.objects.all()
    result=[]
    
    for i in range(len(list)):
        if(list[i]==posts):
            try:
                result.append(list[i-1])
            except:
                result.append('') 
            try:
                result.append(list[i+1])
            except:
                result.append('')        

    content={'posts':posts,'list':result}
   
    return render(request,'blog/blog-single.html',content)

    

def test(request):
    list=Post.objects.all()
    list=Paginator(list,1)
    list=list.get_page(3)
    content={'list':list}
    return render(request,'blog/test.html',content)

def search(request):
    posts=Post.objects.filter(status=1)
    if s:=request.GET.get('search_text'):
        posts=posts.filter(content__contains=s)
    content={'posts':posts}    
    return render(request,'blog/blog-home.html',content)



