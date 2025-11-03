from django.contrib import admin

from .models import Category, Transport, Event, Season, Calendar, TourCalendar


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("name", "active")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "date_start", "date_end", "sort", "active", "public")


@admin.register(Transport)
class TransportAdmin(admin.ModelAdmin):
    list_display = ("name", "active")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_filter = ("day", "category", "season", "public", "active", "fix", "day", "date")
    list_display = (
        "name",
        "day",
        "date",
        "play",
        "public",
        "fix",
        "type",
        "sort",
    )


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('name', 'season', 'register', 'from_date', 'from_time')


@admin.register(TourCalendar)
class TourCalendarAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'from_dt', 'to_dt', 'fetch_events', 'season', 'sort')
    actions = ('reset_periods', 'reset_names')

    @admin.action(description='Reset Periods')
    def reset_periods(self, request, queryset):
        queryset.update(reset_period=True)
        for i in queryset:
            i.save()

    @admin.action(description='Reset Names')
    def reset_names(self, request, queryset):
        queryset.update(reset_name=True)
        for i in queryset:
            i.save()
