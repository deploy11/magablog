from django.contrib import admin
from .models import *
# Register your models here.
class AdminBlog(admin.ModelAdmin):
    list_display = ['id','title','author']

admin.site.register(Blog,AdminBlog)