from django.urls import path,include
from projectApp.views import *

app_name='projectApp'
urlpatterns = [
    # path('',home,name='index'),
    # path('about/',about,name='about'),
    # path('contact/',contact,name='contact'),
    # path('elements/',elements,name='elements'),
    # path('newsletter/',news_letter,name='newsletter')
    path('', IndexView, {'resource': ''}),
    path('<path:resource>', IndexView),
]
#چون مقدار حجم فایل اپلودی زیر 5 مگ بود مجبور شدم فقط همین چندفایلی که تغییر دادم و بفرستم