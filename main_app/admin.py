from django.contrib import admin
from .models import NewsletterSubscriber
from .models import Profile
from django.utils.html import format_html

@admin.register(NewsletterSubscriber)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar_preview')

    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" style="border-radius:5px;" />', obj.avatar.url)
        return "Sem avatar"
    avatar_preview.short_description = 'Avatar'

admin.site.register(Profile, ProfileAdmin)

