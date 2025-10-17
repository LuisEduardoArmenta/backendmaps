#!/usr/bin/env python
"""
Script de prueba para verificar que la API funciona correctamente
"""
import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/markers/"

def test_create_marker():
    """Prueba crear un marcador"""
    data = {
        "nombre": "Test Walmart",
        "categoria": "Supermercado",
        "direccion": "Av. Reforma 3117, Puebla",
        "lat": "19.058223",  # String
        "lng": "-98.223395"  # String
    }
    
    print("📤 Enviando datos:")
    print(json.dumps(data, indent=2))
    
    response = requests.post(BASE_URL, json=data)
    
    print(f"\n📊 Status: {response.status_code}")
    print(f"📦 Respuesta:")
    print(json.dumps(response.json(), indent=2))
    
    return response

def test_list_markers():
    """Prueba listar marcadores"""
    response = requests.get(BASE_URL)
    
    print(f"📊 Status: {response.status_code}")
    print(f"📦 Respuesta:")
    print(json.dumps(response.json(), indent=2))
    
    return response

if __name__ == "__main__":
    print("🧪 Test 1: Listar marcadores")
    print("=" * 50)
    test_list_markers()
    
    print("\n" + "=" * 50)
    print("🧪 Test 2: Crear marcador")
    print("=" * 50)
    test_create_marker()
    
    print("\n" + "=" * 50)
    print("🧪 Test 3: Listar marcadores (después de crear)")
    print("=" * 50)
    test_list_markers()

