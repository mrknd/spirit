from django.contrib import admin
from django.utils.html import format_html

from cars.models import Car


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.car_photo.url}" width="50"/>')

    thumbnail.short_description = 'Photo'

    list_display = ('thumbnail', 'car_title', 'color', 'model', 'year',
                    'state', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('thumbnail', 'car_title', 'color', 'model')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'color', 'model')
    list_filter = ('model', 'fuel_type')


admin.site.register(Car, CarAdmin)
