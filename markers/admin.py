from django.contrib import admin
from .models import Marker


@admin.register(Marker)
class MarkerAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Marker
    """
    
    # Campos que se muestran en la lista
    list_display = [
        'id',
        'nombre',
        'categoria',
        'coordinates_display',
        'created_at_display',
    ]
    
    # Campos por los que se puede filtrar
    list_filter = [
        'categoria',
        'created_at',
        'updated_at',
    ]
    
    # Campos por los que se puede buscar
    search_fields = [
        'nombre',
        'categoria',
        'direccion',
    ]
    
    # Campos de solo lectura
    readonly_fields = [
        'id',
        'created_at',
        'updated_at',
        'coordinates_str',
    ]
    
    # Organización de campos en el formulario
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'categoria')
        }),
        ('Ubicación', {
            'fields': ('direccion', 'lat', 'lng', 'coordinates_str')
        }),
        ('Metadatos', {
            'fields': ('id', 'created_at', 'updated_at'),
            'classes': ('collapse',),  # Sección colapsable
        }),
    )
    
    # Ordenamiento por defecto
    ordering = ['-created_at']
    
    # Número de elementos por página
    list_per_page = 25
    
    # Habilitar acciones en masa
    actions = ['delete_selected_markers', 'export_as_json']
    
    # Métodos personalizados para mostrar en la lista
    
    @admin.display(description='Coordenadas', ordering='lat')
    def coordinates_display(self, obj):
        """Muestra las coordenadas en formato compacto"""
        return f"({obj.lat}, {obj.lng})"
    
    @admin.display(description='Fecha de Creación', ordering='created_at')
    def created_at_display(self, obj):
        """Muestra la fecha en formato legible"""
        return obj.created_at.strftime('%d/%m/%Y %H:%M')
    
    # Acciones personalizadas
    
    @admin.action(description='Eliminar marcadores seleccionados')
    def delete_selected_markers(self, request, queryset):
        """Acción personalizada para eliminar marcadores"""
        count = queryset.count()
        queryset.delete()
        self.message_user(
            request,
            f'{count} marcador(es) eliminado(s) exitosamente.'
        )
    
    @admin.action(description='Exportar como JSON')
    def export_as_json(self, request, queryset):
        """Exporta los marcadores seleccionados como JSON"""
        import json
        from django.http import HttpResponse
        
        markers_data = []
        for marker in queryset:
            markers_data.append({
                'id': marker.id,
                'nombre': marker.nombre,
                'categoria': marker.categoria,
                'direccion': marker.direccion,
                'lat': str(marker.lat),
                'lng': str(marker.lng),
                'created_at': marker.created_at.isoformat(),
            })
        
        response = HttpResponse(
            json.dumps(markers_data, indent=2, ensure_ascii=False),
            content_type='application/json'
        )
        response['Content-Disposition'] = 'attachment; filename="markers.json"'
        return response
    
    def has_add_permission(self, request):
        """Define si se puede agregar marcadores desde el admin"""
        return True
    
    def has_delete_permission(self, request, obj=None):
        """Define si se pueden eliminar marcadores desde el admin"""
        return True


# Personalización del sitio de administración
admin.site.site_header = "Maps Backend - Administración"
admin.site.site_title = "Maps Backend Admin"
admin.site.index_title = "Panel de Control"
