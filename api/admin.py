from django.contrib import admin
from .models import Category, Transport, Event, Season


class SeasonAdmin(admin.ModelAdmin):
    list_display = ("name", "active")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "date_start", "date_end", "sort", "active", "public")


class TransportAdmin(admin.ModelAdmin):
    list_display = ("name", "active")


class EventAdmin(admin.ModelAdmin):

    list_filter = ("day", "category")
    list_display = (
        "name",
        "day",
        "date",
        "season",
        "transport",
        "play",
        "public",
        "active",
        "fix",
        "cert",
        "sort",
    )


admin.site.register(Season, SeasonAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(Event, EventAdmin)
