from rest_framework import viewsets
from rest_framework import permissions
from .models import Category, Evening, Transport, Event, Season
from .serializers import CategorySerializer, EveningSerializer, TransportSerializer, EventSerializer, SeasonSerializer


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


class EveningViewSet(viewsets.ModelViewSet):
    """
    API Endpoint to view Evenings
    """
    queryset = Evening.objects.all().order_by('-date')
    serializer_class = EveningSerializer
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
