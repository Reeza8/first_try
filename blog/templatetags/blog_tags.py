from django import template
from blog.models import Post,Category,Comment
from datetime import datetime
import pytz
register = template.Library()

@register.simple_tag(name='mytag')
def func():
    lp=Post.objects.all()
    return lp

@register.simple_tag(name='date')
def date(date):
    now = datetime.now()
    tz_tehran = pytz.timezone('Asia/Tehran') 
    now = datetime.now(tz_tehran)
    return (now-date).days

@register.simple_tag()
def comment_len(pid):
    return Comment.objects.filter(post_id=pid).count()

@register.inclusion_tag('blog/popular_Posts.html')
def popular_Posts():
    posts=Post.objects.filter(status=1).order_by("-counted_views")[:3]
    return {'posts':posts}

@register.inclusion_tag('blog/Post_categories.html')
def categories():
    temp={}
    category=Category.objects.all()
    posts=Post.objects.filter(status=1)
    for cat in category:
        temp[cat]=posts.filter(category=cat).count()
    return {'categories':temp}
