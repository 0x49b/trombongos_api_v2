import datetime
import json

from django.db.models import Q
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView

from .models import Category, Transport, Event, Season
from .serializers import CategorySerializer, TransportSerializer, EventSerializer, SeasonSerializer
from rest_framework.response import Response


class SeasonViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view Seasons
    """
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view Categories
    """
    queryset = Category.objects.all().order_by('sort')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']


class TransportViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view Transports
    """
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']


class EventViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view Events
    """
    queryset = Event.objects.all().order_by('date', 'play')
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']


class TourViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']

    datetimeformat = ""
    dateformat = "%d.%m.%Y"
    timeformat = "%H:%M"

    def list(self, request, *args, **kwargs):
        season = Season.objects.get(active=True)
        categories = Category.objects.all()

        cats = []

        for cat in categories:
            events = Event.objects.filter(Q(date__gte=datetime.datetime.now()), category=cat, season=season)
            eve = []

            for ev in events:

                warehouse = ev.warehouse
                makeup = ev.makeup
                sun = ev.sun
                if ev.warehouse is not None:
                    warehouse = ev.warehouse.strftime(self.timeformat)
                if ev.makeup is not None:
                    makeup = ev.makeup.strftime(self.timeformat)
                if ev.sun is not None:
                    sun = ev.sun.strftime(self.timeformat)

                e = {
                    "id": ev.uuid,
                    "name": ev.name,
                    "date": ev.date.strftime(self.dateformat),
                    "day": ev.get_day_display(),
                    "ca_makeup": ev.ca_makeup,
                    "makeup": makeup,
                    "warehouse": warehouse,
                    "sun": sun,
                    "gathering": ev.gathering.strftime(self.timeformat),
                    "ca_play": ev.ca_play,
                    "play": ev.play.strftime(self.timeformat),
                    "transport": ev.transport.name,
                    "trailer": ev.trailer,
                    "info": ev.information,
                    "cert": ev.get_cert_display(),
                    "active": ev.active,
                    "public": ev.public,
                    "fix": ev.fix,
                }
                eve.append(e)

            c = {
                "title": cat.name,
                "date_start": cat.date_start.strftime(self.dateformat),
                "date_end": cat.date_end.strftime(self.dateformat),
                "public": cat.public,
                "evening_count": events.count(),
                "evenings": eve
            }

            cats.append(c)

        ret = {
            "season": season.name,
            "requestURL": request.path,
            "requestTime": datetime.datetime.now(),
            "data": cats
        }
        return Response(ret)
