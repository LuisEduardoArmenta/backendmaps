"""
URL configuration for maps_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def api_root(request):
    """
    Vista raíz de la API que muestra información básica y endpoints disponibles
    """
    return JsonResponse({
        'message': 'Bienvenido a Maps Backend API',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'api_markers': '/api/markers/',
            'api_markers_list': '/api/markers/ (GET - Listar marcadores)',
            'api_markers_create': '/api/markers/ (POST - Crear marcador)',
            'api_markers_detail': '/api/markers/{id}/ (GET/PUT/PATCH/DELETE)',
            'api_markers_categorias': '/api/markers/categorias/ (GET - Listar categorías)',
            'api_markers_stats': '/api/markers/stats/ (GET - Estadísticas)',
        },
        'documentation': 'Documentación en /api/markers/ (Django REST Framework Browsable API)'
    })


urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),
    
    # Raíz de la API
    path('', api_root, name='api-root'),
    
    # API de marcadores
    path('api/markers/', include('markers.urls')),
]
