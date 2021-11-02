from django.contrib import admin
from .models import Category, Evening, Transport, Event, Season


class SeasonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "active")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "date_start", "date_end", "sort", "active", "public")


class EveningAdmin(admin.ModelAdmin):
    list_display = ("name", "date", "season", "category")


class TransportAdmin(admin.ModelAdmin):
    list_display = ("name", "active")


class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "season",
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


admin.site.register(Season, SeasonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Evening, EveningAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Event, EventAdmin)
