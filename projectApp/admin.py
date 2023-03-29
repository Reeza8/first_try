from django.contrib import admin
from projectApp.models import Contact,NewsLetter
# Register your models here.


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','subject','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')



@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    pass