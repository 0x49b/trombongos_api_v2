from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'seasons', views.SeasonViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'evenings', views.EveningViewSet)
router.register(r'transports', views.TransportViewSet)
router.register(r'events', views.EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
