from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Marker
from .serializers import MarkerSerializer
from django.http import JsonResponse


class MarkerViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar operaciones CRUD de marcadores.
    
    Endpoints disponibles:
    - GET    /api/markers/          - Listar todos los marcadores
    - POST   /api/markers/          - Crear un nuevo marcador
    - GET    /api/markers/{id}/     - Obtener un marcador específico
    - PUT    /api/markers/{id}/     - Actualizar un marcador completo
    - PATCH  /api/markers/{id}/     - Actualizar parcialmente un marcador
    - DELETE /api/markers/{id}/     - Eliminar un marcador
    """
    
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    
    # Filtros y búsqueda
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['categoria']  # Filtrar por categoría
    search_fields = ['nombre', 'direccion', 'categoria']  # Búsqueda por texto
    ordering_fields = ['created_at', 'nombre', 'categoria']  # Campos para ordenar
    ordering = ['-created_at']  # Orden por defecto: más recientes primero
    
    # healthz moved to module level so it can be imported from urls.py
    

    @action(detail=False, methods=['get'])
    def categorias(self, request):
        """
        Endpoint personalizado para obtener todas las categorías únicas
        GET /api/markers/categorias/
        """
        categorias = Marker.objects.values_list('categoria', flat=True).distinct().order_by('categoria')
        
        return Response({
            'categorias': list(categorias),
            'total': len(categorias)
        })
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """
        Endpoint personalizado para obtener estadísticas
        GET /api/markers/stats/
        """
        from django.db.models import Count
        
        total = Marker.objects.count()
        por_categoria = Marker.objects.values('categoria').annotate(
            cantidad=Count('id')
        ).order_by('-cantidad')
        
        return Response({
            'total_marcadores': total,
            'por_categoria': list(por_categoria),
        })
    
    @action(detail=False, methods=['delete'])
    def delete_all(self, request):
        """
        Endpoint para eliminar todos los marcadores (usar con precaución)
        DELETE /api/markers/delete_all/
        """
        count = Marker.objects.count()
        Marker.objects.all().delete()
        
        return Response({
            'message': f'{count} marcadores eliminados exitosamente',
            'deleted_count': count
        })
    
    @action(detail=False, methods=['post'])
    def bulk_create(self, request):
        """
        Endpoint para crear múltiples marcadores a la vez
        POST /api/markers/bulk_create/
        
        Body: { "markers": [{ marcador1 }, { marcador2 }, ...] }
        """
        markers_data = request.data.get('markers', [])
        
        if not isinstance(markers_data, list):
            return Response(
                {'error': 'Se espera una lista de marcadores'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = MarkerSerializer(data=markers_data, many=True)
        serializer.is_valid(raise_exception=True)
        markers = serializer.save()
        
        return Response({
            'message': f'{len(markers)} marcadores creados exitosamente',
            'data': MarkerSerializer(markers, many=True).data
        }, status=status.HTTP_201_CREATED)


def healthz(request):
    """
    Endpoint de salud a nivel de módulo para uso por herramientas de monitoreo.
    GET /api/markers/healthz/
    """
    return JsonResponse({'status': 'ok'}, status=200)
