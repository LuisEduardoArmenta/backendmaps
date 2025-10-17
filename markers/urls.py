from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MarkerViewSet

# Crear el router para el ViewSet
router = DefaultRouter()
router.register(r'', MarkerViewSet, basename='marker')

# URLs de la app markers
urlpatterns = [
    path('', include(router.urls)),
]

