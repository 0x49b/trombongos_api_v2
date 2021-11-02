from rest_framework import serializers
from .models import Category, Evening, Event, Transport, Season


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ["id", "name", "active", "url"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "date_start", "date_end", "sort", "active", "public", "url"]


class EveningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evening
        fields = ["id", "name", "date", "category", "season", "url"]


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ["id", "name", "active", "url"]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "category",
            "evening",
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
            "season",
            "public",
            "active",
            "fix",
            "url"
        ]


class TourSerializer(serializers.ModelSerializer):
    evening = EveningSerializer(read_only=False, many=False)
    transport = TransportSerializer(read_only=False, many=False)
    category = CategorySerializer(read_only=False, many=False)
    season = SeasonSerializer(read_only=False, many=False)

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "category",
            "evening",
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
            "season",
            "public",
            "active",
            "fix",
            "url"
        ]
