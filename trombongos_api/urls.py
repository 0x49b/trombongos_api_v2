from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import views
from . import views as core_views
from .feeds import EventFeed

router = routers.DefaultRouter()
router.register(r'seasons', views.SeasonViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'transports', views.TransportViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'tour', views.TourViewSet, basename='tour')

urlpatterns = [
    path('', core_views.root_view),
    path('admin/', admin.site.urls),
    path('saison/feed.ics', EventFeed()),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
