from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Post,Comment

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title','draft','author']
    list_filter = ['title','draft']
    search_fields = ['title','draft']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['user','post','created_dt'] 
    list_filter =['user']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)

