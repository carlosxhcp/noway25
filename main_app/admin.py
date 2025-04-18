from django.contrib import admin
from .models import NewsletterSubscriber

@admin.register(NewsletterSubscriber)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)