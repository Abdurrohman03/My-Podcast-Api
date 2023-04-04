from django.contrib import admin
from .models import Category, Tag, Blog, CommentBlog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_date']
    date_hierarchy = 'created_date'
    list_display_links = ['id', 'title', 'created_date']
    search_fields = ['title', 'author__username', 'author__first_name', 'author__last_name']
    ordering = ['-id']
    filter_horizontal = ['tags']


admin.site.register(CommentBlog)
