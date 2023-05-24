from django.contrib import admin
from .models import Category, SubCategory, Tag, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Post)
