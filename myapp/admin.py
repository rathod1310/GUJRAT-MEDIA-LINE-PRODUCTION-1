from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(Contact_Us)
class LeaveACommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject' ,'message')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" width="60" />', obj.image.url)
    display_image.short_description = 'Image'

@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ('serial_name', 'display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" width="60" />', obj.image.url)
    display_image.short_description = 'Image'

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('advertisement_name', 'display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" width="60" />', obj.image.url)
    display_image.short_description = 'Image'

@admin.register(Web_series)
class Web_seriesAdmin(admin.ModelAdmin):
    list_display = ('web_series_name', 'display_image')

    def display_image(self, obj):
        return format_html('<img src="{}" width="60" />', obj.image.url)
    display_image.short_description = 'Image'