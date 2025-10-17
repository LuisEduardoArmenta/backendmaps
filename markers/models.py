from django.db import models

class Marker(models.Model):
    """
    Modelo para almacenar información de marcadores de ubicaciones en el mapa.
    
    Campos:
    - nombre: Nombre del negocio o ubicación
    - categoria: Categoría del negocio (ej: Restaurante, Tienda, Hotel)
    - direccion: Dirección completa de la ubicación
    - lat: Latitud (coordenada geográfica)
    - lng: Longitud (coordenada geográfica)
    - created_at: Fecha y hora de creación (automático)
    - updated_at: Fecha y hora de última actualización (automático)
    """
    
    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre del negocio",
        help_text="Nombre del negocio o ubicación"
    )
    
    categoria = models.CharField(
        max_length=100,
        verbose_name="Categoría",
        help_text="Categoría del negocio (ej: Restaurante, Cafetería, Hotel)"
    )
    
    direccion = models.TextField(
        verbose_name="Dirección",
        help_text="Dirección completa de la ubicación"
    )
    
    lat = models.DecimalField(
        max_digits=12,
        decimal_places=9,
        verbose_name="Latitud",
        help_text="Latitud de la ubicación (coordenada geográfica)"
    )
    
    lng = models.DecimalField(
        max_digits=12,
        decimal_places=9,
        verbose_name="Longitud",
        help_text="Longitud de la ubicación (coordenada geográfica)"
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación"
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización"
    )
    
    class Meta:
        verbose_name = "Marcador"
        verbose_name_plural = "Marcadores"
        ordering = ['-created_at']  # Ordenar por más recientes primero
        indexes = [
            models.Index(fields=['lat', 'lng']),  # Índice para búsquedas por coordenadas
            models.Index(fields=['categoria']),    # Índice para filtros por categoría
        ]
    
    def __str__(self):
        """
        Representación en string del marcador
        """
        return f"{self.nombre} ({self.categoria}) - {self.lat}, {self.lng}"
    
    def get_coordinates(self):
        """
        Retorna las coordenadas como diccionario
        """
        return {
            'lat': float(self.lat),
            'lng': float(self.lng)
        }
    
    @property
    def coordinates_str(self):
        """
        Retorna las coordenadas como string formateado
        """
        return f"{self.lat}, {self.lng}"
