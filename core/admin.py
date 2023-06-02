from django.contrib import admin
from django.utils.html import format_html
from .models import Category, SubCategory, Tag, Post, Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'view_subcategories', 'view_posts_count']
    list_display_links = ['id', 'name']
    search_fields = ['name']

    def view_subcategories(self, obj):
        href = f'/admin/core/subcategory/?category__id__exact={obj.id}'
        url = f'<a href="{href}">{obj.subcategories.count()} подкатегорий</a>'
        return format_html(url)
    view_subcategories.short_description = 'Количество подкатегорий'

    def view_posts_count(self, obj):
        posts_count = 0
        for subcategory in obj.subcategories.all():
            posts_count += subcategory.posts.count()
        return f'{posts_count} постов'
    view_posts_count.short_description = 'Количество постов'


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'view_posts_count']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    list_filter = ['category']
    raw_id_fields = ['category']
    autocomplete_fields = ['category']


    def view_posts_count(self, obj):
        return obj.posts.count()
    view_posts_count.short_description = 'Количество постов'


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'view_posts_count']
    list_display_links = ['id', 'name']
    search_fields = ['name']

    def view_posts_count(self, obj):
        return obj.posts.count()
    view_posts_count.short_description = 'Количество постов'


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'view_text', 'subcategory', 'view_tags', 'created_at', 'updated_at', 'view_comments']
    list_display_links = ['id', 'title', 'view_text']
    search_fields = ['title', 'text']
    list_filter = ['subcategory', 'tags', 'created_at']


    # def view_tags(self, obj):
    #     return ', '.join([tag.name for tag in obj.tags.all()])

    def view_tags(self, obj):
        urls = []
        for tag in obj.tags.all():
            urls.append(f'<a href="/admin/core/tag/{tag.id}/change/">{tag.name}</a><br>')
        return format_html(' '.join(urls))
    view_tags.short_description = 'Теги'


    def view_text(self, obj):
        return f'{obj.text[:50]}...'
    view_text.short_description = 'Текст'


    def view_comments(self, obj):
        url = f'/admin/core/comment/?post__id__exact={obj.id}'
        return format_html(f'<a href="{url}">{obj.comments.count()} комментариев</a>')
    view_comments.short_description = 'Количество комментариев'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'author', 'text', 'created_at']
    list_display_links = ['id', 'post']
    search_fields = ['post__title', 'author__name', 'text']
    list_filter = ['created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)


# 3. Добавить view 
