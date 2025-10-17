from rest_framework import serializers
from .models import Marker


class MarkerSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo Marker.
    
    Convierte los objetos Marker a JSON y viceversa para la API REST.
    Incluye validaciones personalizadas para coordenadas.
    """
    
    class Meta:
        model = Marker
        fields = [
            'id',
            'nombre',
            'categoria',
            'direccion',
            'lat',
            'lng',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_lat(self, value):
        """
        Valida que la latitud esté en el rango válido
        """
        if value < -90 or value > 90:
            raise serializers.ValidationError(
                "La latitud debe estar entre -90 y 90 grados."
            )
        return value
    
    def validate_lng(self, value):
        """
        Valida que la longitud esté en el rango válido
        """
        if value < -180 or value > 180:
            raise serializers.ValidationError(
                "La longitud debe estar entre -180 y 180 grados."
            )
        return value
    
    def validate(self, data):
        """
        Validaciones a nivel de objeto completo
        """
        # Validar que no se repitan exactamente las mismas coordenadas y nombre
        if self.instance is None:  # Solo en creación
            if Marker.objects.filter(
                nombre=data.get('nombre'),
                lat=data.get('lat'),
                lng=data.get('lng')
            ).exists():
                raise serializers.ValidationError(
                    "Ya existe un marcador con el mismo nombre en estas coordenadas."
                )
        
        return data


class MarkerListSerializer(serializers.ModelSerializer):
    """
    Serializer simplificado para listados de marcadores.
    Solo incluye los campos esenciales para mejor rendimiento.
    """
    
    class Meta:
        model = Marker
        fields = [
            'id',
            'nombre',
            'categoria',
            'lat',
            'lng',
        ]


class MarkerCreateSerializer(serializers.ModelSerializer):
    """
    Serializer específico para la creación de marcadores.
    Puede incluir validaciones adicionales específicas para creación.
    """
    
    class Meta:
        model = Marker
        fields = [
            'nombre',
            'categoria',
            'direccion',
            'lat',
            'lng',
        ]
    
    def create(self, validated_data):
        """
        Crea y retorna una nueva instancia de Marker
        """
        return Marker.objects.create(**validated_data)

