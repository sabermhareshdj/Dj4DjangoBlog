from django.contrib import admin

# Register your models here.
from .models import Post,Commment

admin.site.register(Post)
admin.site.register(Commment)

