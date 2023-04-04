from django.contrib import admin
from .models import Podcast, Comment, Season, Like


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_date']
    date_hierarchy = 'created_date'
    list_display_links = ['id', 'title', 'created_date']
    search_fields = ['title', 'author__username', 'author__first_name', 'author__last_name']
    ordering = ['-id']
    filter_horizontal = ['tags']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_date']
    search_fields = ['article', 'author__username', 'author__first_name', 'author__last_name']


admin.site.register(Season)
admin.site.register(Like)

