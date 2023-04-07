from django.urls import path,include
from resume.views import *
# from blog.feeds import LatestEntriesFeed

app_name='resume'

urlpatterns = [
    path('',home,name='index'),
]
