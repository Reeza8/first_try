from django import template
from blog.models import Post,Category
from django.core.paginator import Paginator
from datetime import datetime, timedelta
import pytz

register = template.Library()

@register.inclusion_tag('projectApp/latest_posts.html')
def latest_posts():
    posts=Post.objects.filter(status=1).order_by('-published_date')[:6]
    return {'posts':posts}



