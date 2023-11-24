from django.contrib import admin
from core.models import Event, Gift, WebConfig


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(WebConfig)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['site_name']