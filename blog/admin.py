from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from .models import Post,Comment

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['title','draft','author']
    list_filter = ['title','draft']
    search_fields = ['title','draft']
admin.site.register(Post,PostAdmin)
admin.site.register(Comment)

