# 📁 Estructura del Backend Django

## 🌳 Árbol de Directorios

```
backend/
├── 📁 venv/                           # Virtual Environment
│
├── 📁 maps_backend/                   # Proyecto Django Principal
│   ├── __init__.py
│   ├── ⚙️ settings.py                 # Configuración (MySQL, CORS, DRF)
│   ├── 🔗 urls.py                     # URLs principales
│   ├── wsgi.py                        # WSGI para deployment
│   └── asgi.py                        # ASGI para async
│
├── 📁 markers/                        # App de Marcadores
│   ├── 📁 migrations/
│   │   ├── __init__.py
│   │   └── ✅ 0001_initial.py         # Migración del modelo Marker
│   │
│   ├── __init__.py
│   ├── 🎨 admin.py                    # Panel de administración
│   ├── apps.py                        # Config de la app
│   ├── 📊 models.py                   # Modelo Marker
│   ├── 🔄 serializers.py              # Serializers para API
│   ├── 🎯 views.py                    # ViewSet con endpoints
│   ├── 🔗 urls.py                     # URLs de la API
│   └── tests.py                       # Tests unitarios
│
├── 📄 manage.py                       # Script de gestión
├── 📦 requirements.txt                # Dependencias
├── 🚫 .gitignore                      # Archivos a ignorar
│
└── 📚 Documentación/
    ├── README.md                      # Documentación completa
    ├── INICIO_RAPIDO.md               # Guía rápida (5 min)
    ├── INTEGRACION_FRONTEND.md        # Conectar con Angular
    └── ESTRUCTURA.md                  # Este archivo
```

---

## 📊 Componentes Principales

### 1. settings.py - Configuración

```python
✅ ALLOWED_HOSTS = ['*']               # Para desarrollo
✅ INSTALLED_APPS:
    - rest_framework                   # Django REST Framework
    - corsheaders                      # CORS Headers
    - django_filters                   # Filtros
    - markers                          # App de marcadores

✅ MIDDLEWARE:
    - corsheaders.middleware.CorsMiddleware  # CORS

✅ DATABASES:
    - MySQL (configurado para nube)

✅ CORS_ALLOW_ALL_ORIGINS = True       # Para desarrollo
✅ REST_FRAMEWORK (configurado)
```

---

### 2. models.py - Modelo Marker

```python
class Marker(models.Model):
    id          → Integer (Auto)       # Primary Key
    nombre      → CharField(200)       # Nombre del negocio
    categoria   → CharField(100)       # Categoría
    direccion   → TextField            # Dirección completa
    lat         → DecimalField(10,6)   # Latitud
    lng         → DecimalField(10,6)   # Longitud
    created_at  → DateTimeField        # Fecha de creación
    updated_at  → DateTimeField        # Última actualización
```

**Métodos:**
- `__str__()` - Representación en string
- `get_coordinates()` - Retorna dict con coordenadas
- `coordinates_str` - Property con coordenadas formateadas

**Metadatos:**
- Ordenamiento por `-created_at`
- Índices en `lat/lng` y `categoria`

---

### 3. serializers.py - Serializers

```python
MarkerSerializer          → Serializer completo
    - Todos los campos
    - Campos calculados (coordinates_str, created_at_formatted)
    - Validaciones de lat/lng (-90 a 90, -180 a 180)

MarkerListSerializer      → Para listados (optimizado)
    - Solo campos esenciales

MarkerCreateSerializer    → Para creación
    - Solo campos necesarios para crear
```

---

### 4. views.py - ViewSet

```python
MarkerViewSet → ViewSet completo con:

📍 Endpoints CRUD:
    GET     /api/markers/          → Listar
    POST    /api/markers/          → Crear
    GET     /api/markers/{id}/     → Detalle
    PUT     /api/markers/{id}/     → Actualizar completo
    PATCH   /api/markers/{id}/     → Actualizar parcial
    DELETE  /api/markers/{id}/     → Eliminar

📊 Endpoints Adicionales:
    GET     /api/markers/categorias/      → Categorías únicas
    GET     /api/markers/stats/           → Estadísticas
    POST    /api/markers/bulk_create/     → Crear múltiples
    DELETE  /api/markers/delete_all/      → Eliminar todos

🔍 Funcionalidades:
    - Filtros por categoría
    - Búsqueda por texto (nombre, dirección, categoría)
    - Ordenamiento por múltiples campos
    - Paginación (100 items por página)
```

---

### 5. admin.py - Panel de Administración

```python
@admin.register(Marker)
class MarkerAdmin:
    
    📋 Lista:
        - ID, nombre, categoría, coordenadas, fecha
    
    🔍 Búsqueda:
        - Por nombre, categoría, dirección
    
    🎛️ Filtros:
        - Por categoría, fecha de creación
    
    ⚙️ Acciones Personalizadas:
        - Eliminar marcadores seleccionados
        - Exportar como JSON
    
    📝 Formulario:
        - Organizado en fieldsets
        - Campos de solo lectura
```

---

### 6. urls.py - Configuración de URLs

```python
Backend Principal (maps_backend/urls.py):
    /                  → API Root (info)
    /admin/            → Panel de administración
    /api/markers/      → Include markers.urls

App Markers (markers/urls.py):
    /                  → MarkerViewSet (router)
        ├── GET    /                    → list()
        ├── POST   /                    → create()
        ├── GET    /{id}/               → retrieve()
        ├── PUT    /{id}/               → update()
        ├── PATCH  /{id}/               → partial_update()
        ├── DELETE /{id}/               → destroy()
        ├── GET    /categorias/         → categorias()
        ├── GET    /stats/              → stats()
        ├── POST   /bulk_create/        → bulk_create()
        └── DELETE /delete_all/         → delete_all()
```

---

## 📦 Dependencias (requirements.txt)

```
Django==5.2.7                  → Framework web
djangorestframework==3.16.1    → API REST
mysqlclient==2.2.7             → Conector MySQL
django-cors-headers==4.9.0     → Manejo de CORS
django-filter==25.2            → Filtros para DRF
asgiref==3.10.0                → Soporte async
sqlparse==0.5.3                → Parser SQL
tzdata==2025.2                 → Datos de zonas horarias
```

---

## 🔄 Flujo de Datos

```
┌─────────────────────────────────────────────────────────────┐
│                    REQUEST DE FRONTEND                       │
│              (Angular hace HTTP Request)                     │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                  DJANGO URLs (urls.py)                       │
│              Route: /api/markers/                            │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                 VIEWSET (views.py)                           │
│         MarkerViewSet.create() / list() / etc.               │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│              SERIALIZER (serializers.py)                     │
│         Validación y transformación de datos                 │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                  MODEL (models.py)                           │
│            Operaciones en base de datos                      │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                 MYSQL DATABASE                               │
│              (Base de datos en la nube)                      │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                    RESPONSE JSON                             │
│              (Django envía respuesta)                        │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│                FRONTEND ACTUALIZA UI                         │
│            (Angular muestra los datos)                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 Endpoints Organizados

### Endpoints CRUD Básicos

| Método | URL | ViewSet Method | Descripción |
|--------|-----|----------------|-------------|
| GET | `/api/markers/` | `list()` | Listar marcadores |
| POST | `/api/markers/` | `create()` | Crear marcador |
| GET | `/api/markers/{id}/` | `retrieve()` | Ver detalle |
| PUT | `/api/markers/{id}/` | `update()` | Actualizar completo |
| PATCH | `/api/markers/{id}/` | `partial_update()` | Actualizar parcial |
| DELETE | `/api/markers/{id}/` | `destroy()` | Eliminar |

### Endpoints Personalizados (@action)

| Método | URL | ViewSet Method | Descripción |
|--------|-----|----------------|-------------|
| GET | `/api/markers/categorias/` | `categorias()` | Categorías únicas |
| GET | `/api/markers/stats/` | `stats()` | Estadísticas |
| POST | `/api/markers/bulk_create/` | `bulk_create()` | Crear múltiples |
| DELETE | `/api/markers/delete_all/` | `delete_all()` | Eliminar todos |

---

## 🔐 Seguridad Implementada

```
✅ CSRF Protection (Django)
✅ CORS configurado (django-cors-headers)
✅ Validaciones en serializers
✅ SQL Injection Protection (ORM)
✅ Permisos configurables (AllowAny para desarrollo)
```

**Para Producción:**
```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com']
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = ['https://tu-frontend.com']
```

---

## 📈 Características Avanzadas

### Paginación
```python
PAGE_SIZE = 100  # 100 marcadores por página
```

### Filtros
```python
?categoria=Restaurante           # Filtrar por categoría
?search=café                     # Búsqueda de texto
?ordering=-created_at            # Ordenar por fecha desc
?ordering=nombre                 # Ordenar por nombre asc
```

### Búsqueda
```python
search_fields = ['nombre', 'direccion', 'categoria']
```

---

## ✅ Estado Actual

```
✅ Virtual environment creado
✅ Dependencias instaladas
✅ Proyecto Django configurado
✅ App markers creada
✅ Modelo Marker definido
✅ Serializers creados
✅ ViewSet completo
✅ URLs configuradas
✅ Admin configurado
✅ Migraciones creadas
✅ CORS configurado
✅ Documentación completa
```

---

## 🚀 Listo para Usar

El backend está **100% funcional** y listo para:
1. Recibir peticiones del frontend Angular
2. Guardar datos en MySQL
3. Servir datos via API REST
4. Gestionar marcadores desde el panel admin

**¡Empieza a usarlo siguiendo `INICIO_RAPIDO.md`!** 🎉

