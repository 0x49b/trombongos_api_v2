from django.contrib import admin
from .models import Category, Evening, Transport, Event


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_start", "date_end", "sort", "active", "public")


class EveningAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "category")


class TransportAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "active")


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "date",
        "transport",
        "ca_makeup",
        "makeup",
        "warehouse",
        "sun",
        "gathering",
        "ca_play",
        "play",
        "trailer",
        "information",
        "public",
        "active",
        "fix",
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Evening, EveningAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Event, EventAdmin)
