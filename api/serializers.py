from rest_framework import serializers

from .models import Category, Event, Transport, Season


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ["id", "name", "active", "url"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "date_start", "date_end", "sort", "active", "public", "url"]


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = ["id", "name", "active", "url"]


class EventSerializer(serializers.ModelSerializer):
    cert = serializers.CharField(source='get_cert_display')
    transport = serializers.CharField(source='transport.name')
    date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = Event
        fields = [
            "uuid",
            "name",
            "date",
            "day",
            "transport",
            "ca_makeup",
            "makeup",
            "warehouse",
            "sun",
            "gathering",
            "ca_play",
            "play",
            "departure_home",
            "trailer",
            "information",
            "public",
            "active",
            "fix",
            "cert",
            "url"
        ]
