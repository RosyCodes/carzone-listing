from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    # creates a photo thumbnail
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px" />'.format(object.photo.url))

    # changes the label
    thumbnail.short_description = 'Photo'

    # displays these fields on the admin dashboard
    list_display = ('id', 'thumbnail', 'first_name', 'last_name',
                    'designation', 'created_date')

    # displays clickable fields
    list_display_links = ('id', 'first_name', 'thumbnail',)

    # displays search bar based on the following fields
    search_fields = ('last_name', 'first_name', 'designation')

    # creates a filter
    list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
