from rest_framework import serializers
from .models import Category, Evening, Event, Transport


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "date_start", "date_end", "sort", "active", "public", "url"]


class EveningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evening
        fields = ["id", "name", "date", "category", "url"]


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
            "public",
            "active",
            "fix",
            "url"
        ]
