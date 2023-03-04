from django.urls import path,include
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',home,name='home'),
    path('single/',single,name='single'),

]
