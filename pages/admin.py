from django.contrib import admin
from django.utils.html import format_html

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html(f'<img src="{object.photo.url}" width="40" style="border-radius:50px;"/>')

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_at')
    list_display_links = ('id', 'thumbnail', 'first_name', 'last_name', 'designation')
    search_fields = ('id', 'first_name', 'last_name', 'designation')
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
