from django.contrib import admin
from core.models import Event, Gift


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
