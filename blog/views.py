from django.shortcuts import render,get_object_or_404
from django.http import *
from blog.models import Post
from datetime import *
import pytz



def home(request):
    #check the published date and add it if its pass
    posts=Post.objects.all()
    tz_tehran = pytz.timezone('Asia/Tehran') 
    datetime_Karachi = datetime.now(tz_tehran)
    for post in posts:
        if(post.published_date<datetime_Karachi):
            post.status=1
            post.save()


    posts=Post.objects.filter(status=1)
    content={'posts':posts}
    return render(request,'blog/blog-home.html',content)


def single2(request,pid):
    posts=get_object_or_404(Post,pk=pid,status=1)
    posts.counted_views+=1
    posts.save()
    content={'posts':posts}
    return render(request,'blog/blog-single.html',content)

def test(request,pid):
    post=Post.objects.get(id=pid)
    content={'syr':post}
    return render(request,'blog/test.html',content)



