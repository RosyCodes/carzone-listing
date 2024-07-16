from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    # creates a photo thumbnail
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.car_photo.url))

    # changes the label
    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year',
                    'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    search_fields = ('car_title', 'city', 'model', 'body_style', 'fuel_type')

    # editable  boolean field
    list_editable = ('is_featured'),

    list_filter = ('city', 'model', 'body_style', 'fuel_type')


# Register your models here.
admin.site.register(Car, CarAdmin)
