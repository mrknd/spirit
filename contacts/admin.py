from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'phone', 'car_title', 'create_date')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'car_title')
    list_per_page = 20


admin.site.register(Contact, ContactAdmin)
