from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from blog.models import Post,Category,Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('title' ,'author','counted_views','status','id','published_date','created_date')
    search_fields = ['title','content']
    list_filter = ('status',)
    empty_value_display = '-empty-'
    summernote_fields = ('content',)

admin.site.register(Category)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name' ,'post','status','created_date')
    search_fields = ['name','post']
    list_filter = ('status','name')
    empty_value_display = '-empty-'
    


