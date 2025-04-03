
from django.contrib import admin
from .models import Posts, Category, About

class postAdmin(admin.ModelAdmin):
    list_filter =('category', "created_at")
admin.site.register(Posts, postAdmin)
admin.site.register(Category)
admin.site.register(About)