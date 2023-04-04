from django.shortcuts import render,get_object_or_404
from django.http import *
from blog.models import Post,Comment
from blog.forms import CommentForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from datetime import *
import pytz
from django.contrib import messages


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
    if kwargs.get('tag_name')!=None:
        posts=posts.filter(tags__name__in=[kwargs.get('tag_name')])

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
    
    
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment saved succefully') 
        else:
            messages.error(request, 'Your comment did not saved') 


    posts=get_object_or_404(Post,pk=pid,status=1)
    #add counted view
    posts.counted_views+=1
    posts.save()
   

    #next and previos post
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


    comments=Comment.objects.filter(post_id=pid,status=True).order_by('-created_date')
    form=CommentForm()
    content={'posts':posts,'list':result,'comments':comments,'form':form}
   
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



