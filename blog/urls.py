from django.urls import path,include
from blog.views import *
from blog.feeds import LatestEntriesFeed

app_name='blog'

urlpatterns = [

    path('',home,name='home'),

    path('<int:pid>',single2,name='single'),

    path('category/<str:catname>',home,name='category'),
    
    path('author/<str:author>',home,name='author'),

    path('tag/<str:tag_name>',home,name='tag'),

    path('search/',search,name='search'),

    path('test/',test),

    path('rss-feed/', LatestEntriesFeed()),
    
]
