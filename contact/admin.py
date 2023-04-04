from django.contrib import admin
from .models import Contact, Newsletter


admin.site.register(Contact)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
