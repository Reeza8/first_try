from django.contrib import admin

# Register your models here.
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title' ,'author','counted_views','status','id','published_date','created_date')
    search_fields = ['title','content']
    list_filter = ('status',)
    empty_value_display = '-empty-'
    




