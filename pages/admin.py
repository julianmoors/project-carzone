from django.contrib import admin
from django.utils.html import format_html

from . models import Member

class MemberAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50%">'.format(object.photo.url))

    search_fields = ('first_name', 'last_name', 'job_title')
    thumbnail.short_description = 'Photo'

    list_display = ('thumbnail', 'first_name', 'last_name', 'job_title')
    list_display_links = ('thumbnail', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name', 'job_title')

admin.site.register(Member, MemberAdmin)
