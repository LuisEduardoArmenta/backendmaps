# 🗺️ Maps Backend - Django REST API

Backend Django para gestionar marcadores de ubicaciones con Google Maps.

## 📋 Características

- ✅ API REST completa para marcadores (CRUD)
- ✅ Conexión a MySQL en la nube
- ✅ Django REST Framework
- ✅ CORS habilitado para frontend Angular
- ✅ Panel de administración de Django
- ✅ Filtros y búsqueda avanzada
- ✅ Validaciones personalizadas
- ✅ Endpoints adicionales (stats, categorías, bulk operations)

---

## 🚀 Configuración Inicial

### 1. Configurar Base de Datos MySQL

⚠️ **IMPORTANTE:** Antes de ejecutar el proyecto, debes configurar tus credenciales de MySQL.

Edita `maps_backend/settings.py` y reemplaza las siguientes líneas:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tu_nombre_de_base_de_datos',      # Ejemplo: 'maps_db'
        'USER': 'tu_usuario',                      # Ejemplo: 'u123456789_maps'
        'PASSWORD': 'tu_password',                 # Tu contraseña real
        'HOST': 'tu_host.mysql.database',         # Ejemplo: 'srv1234.hostinger.com'
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

### 2. Activar Virtual Environment

#### Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

#### macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Instalar Dependencias (Si no lo hiciste)

```bash
pip install -r requirements.txt
```

### 4. Ejecutar Migraciones

Una vez configurada la base de datos, ejecuta:

```bash
python manage.py migrate
```

Este comando creará todas las tablas necesarias en tu base de datos MySQL.

### 5. Crear Superusuario (Opcional)

Para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu usuario administrador.

### 6. Ejecutar el Servidor

```bash
python manage.py runserver
```

El servidor estará disponible en: **http://127.0.0.1:8000**

---

## 📍 Endpoints de la API

### Base URL: `http://127.0.0.1:8000/api/markers/`

### Endpoints Principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/markers/` | Listar todos los marcadores |
| POST | `/api/markers/` | Crear un nuevo marcador |
| GET | `/api/markers/{id}/` | Obtener un marcador específico |
| PUT | `/api/markers/{id}/` | Actualizar un marcador completo |
| PATCH | `/api/markers/{id}/` | Actualizar parcialmente un marcador |
| DELETE | `/api/markers/{id}/` | Eliminar un marcador |

### Endpoints Adicionales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/markers/categorias/` | Listar categorías únicas |
| GET | `/api/markers/stats/` | Estadísticas de marcadores |
| POST | `/api/markers/bulk_create/` | Crear múltiples marcadores |
| DELETE | `/api/markers/delete_all/` | Eliminar todos los marcadores |

---

## 📝 Ejemplos de Uso

### 1. Crear un Marcador

**Request:**
```http
POST /api/markers/
Content-Type: application/json

{
  "nombre": "Café La Parroquia",
  "categoria": "Cafetería",
  "direccion": "Av. Juárez 123, Puebla, México",
  "lat": 19.0433,
  "lng": -98.2019
}
```

**Response:**
```json
{
  "message": "Marcador creado exitosamente",
  "data": {
    "id": 1,
    "nombre": "Café La Parroquia",
    "categoria": "Cafetería",
    "direccion": "Av. Juárez 123, Puebla, México",
    "lat": "19.043300",
    "lng": "-98.201900",
    "coordinates_str": "19.043300, -98.201900",
    "created_at": "2024-01-15T10:30:00Z",
    "created_at_formatted": "15/01/2024 10:30",
    "updated_at": "2024-01-15T10:30:00Z"
  }
}
```

### 2. Listar Marcadores

**Request:**
```http
GET /api/markers/
```

**Response:**
```json
{
  "count": 10,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "nombre": "Café La Parroquia",
      "categoria": "Cafetería",
      "lat": "19.043300",
      "lng": "-98.201900"
    },
    ...
  ]
}
```

### 3. Filtrar por Categoría

**Request:**
```http
GET /api/markers/?categoria=Restaurante
```

### 4. Buscar por Texto

**Request:**
```http
GET /api/markers/?search=café
```

### 5. Obtener Estadísticas

**Request:**
```http
GET /api/markers/stats/
```

**Response:**
```json
{
  "total_marcadores": 25,
  "por_categoria": [
    {
      "categoria": "Restaurante",
      "cantidad": 10
    },
    {
      "categoria": "Cafetería",
      "cantidad": 8
    },
    {
      "categoria": "Hotel",
      "cantidad": 7
    }
  ]
}
```

### 6. Eliminar un Marcador

**Request:**
```http
DELETE /api/markers/1/
```

**Response:**
```json
{
  "message": "Marcador eliminado exitosamente",
  "deleted": {
    "id": 1,
    "nombre": "Café La Parroquia",
    "categoria": "Cafetería"
  }
}
```

---

## 🎨 Panel de Administración

Accede al panel en: **http://127.0.0.1:8000/admin/**

### Características del Admin

- ✅ Lista completa de marcadores
- ✅ Búsqueda por nombre, categoría y dirección
- ✅ Filtros por categoría y fecha
- ✅ Exportar marcadores como JSON
- ✅ Acciones en masa
- ✅ Vista detallada de cada marcador

---

## 🔧 Modelo de Datos

### Marker

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | Integer (Auto) | ID único del marcador |
| nombre | CharField(200) | Nombre del negocio |
| categoria | CharField(100) | Categoría del negocio |
| direccion | TextField | Dirección completa |
| lat | DecimalField(10,6) | Latitud |
| lng | DecimalField(10,6) | Longitud |
| created_at | DateTimeField | Fecha de creación |
| updated_at | DateTimeField | Última actualización |

---

## 🌐 Configuración de CORS

Por defecto, CORS está configurado para permitir todas las solicitudes (desarrollo):

```python
CORS_ALLOW_ALL_ORIGINS = True
```

**Para producción**, actualiza `settings.py`:

```python
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",           # Angular en desarrollo
    "https://tu-dominio-frontend.com", # Tu dominio en producción
]

CORS_ALLOW_CREDENTIALS = True
```

---

## 📦 Estructura del Proyecto

```
backend/
├── venv/                      # Virtual environment
├── maps_backend/              # Proyecto Django principal
│   ├── __init__.py
│   ├── settings.py           # ⚙️ Configuración (MySQL, CORS, DRF)
│   ├── urls.py               # 🔗 URLs principales
│   ├── wsgi.py
│   └── asgi.py
├── markers/                   # App de marcadores
│   ├── migrations/
│   │   └── 0001_initial.py   # ✅ Migración creada
│   ├── __init__.py
│   ├── admin.py              # 🎨 Configuración del admin
│   ├── apps.py
│   ├── models.py             # 📊 Modelo Marker
│   ├── serializers.py        # 🔄 Serializers para API
│   ├── views.py              # 🎯 ViewSet con endpoints
│   ├── urls.py               # 🔗 URLs de la API
│   └── tests.py
├── manage.py                  # Script de gestión de Django
├── requirements.txt           # 📦 Dependencias
└── README.md                  # 📖 Esta documentación
```

---

## 📚 Dependencias Instaladas

```
Django==5.2.7                  # Framework web
djangorestframework==3.16.1    # API REST
mysqlclient==2.2.7             # Conector MySQL
django-cors-headers==4.9.0     # Manejo de CORS
django-filter==25.2            # Filtros para DRF
```

---

## 🧪 Probar la API

### Usando curl

```bash
# Crear marcador
curl -X POST http://127.0.0.1:8000/api/markers/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Test Location",
    "categoria": "Test",
    "direccion": "Test Address",
    "lat": 19.0433,
    "lng": -98.2019
  }'

# Listar marcadores
curl http://127.0.0.1:8000/api/markers/
```

### Usando Postman

1. Importa la URL base: `http://127.0.0.1:8000/api/markers/`
2. Configura el método (GET, POST, PUT, DELETE)
3. Para POST/PUT, agrega el body en formato JSON
4. Headers: `Content-Type: application/json`

### Usando el Navegador

Accede a: **http://127.0.0.1:8000/api/markers/**

Django REST Framework proporciona una interfaz web navegable donde puedes:
- Ver la lista de marcadores
- Crear nuevos marcadores usando un formulario
- Probar todos los endpoints
- Ver la documentación automática

---

## 🚀 Despliegue en Producción

### Preparar para Hostinger (VPS)

1. **Actualizar `settings.py`:**

```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com', 'IP_DEL_VPS']

# Configurar CORS para producción
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://tu-frontend.com",
]

# Configurar archivos estáticos
STATIC_ROOT = '/home/usuario/static/'
```

2. **Recolectar archivos estáticos:**

```bash
python manage.py collectstatic
```

3. **Configurar Gunicorn:**

```bash
pip install gunicorn
gunicorn maps_backend.wsgi:application --bind 0.0.0.0:8000
```

4. **Configurar Nginx o Apache como proxy inverso**

---

## 🐛 Troubleshooting

### Error: "Unknown server host"

**Causa:** Las credenciales de MySQL no están configuradas.

**Solución:** Edita `settings.py` y configura tus credenciales de MySQL reales.

### Error: "No module named 'mysqlclient'"

**Solución:**
```bash
pip install mysqlclient
```

### Error: "CORS error" en el frontend

**Solución:** Verifica que `django-cors-headers` esté en `INSTALLED_APPS` y `MIDDLEWARE`.

### Error: "Table doesn't exist"

**Solución:** Ejecuta las migraciones:
```bash
python manage.py migrate
```

---

## 📞 Soporte

Si tienes problemas:

1. Verifica que el virtual environment esté activado
2. Verifica que todas las dependencias estén instaladas
3. Verifica las credenciales de MySQL
4. Revisa los logs del servidor

---

## ✅ Checklist de Verificación

- [ ] Virtual environment activado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] Credenciales de MySQL configuradas en `settings.py`
- [ ] Migraciones ejecutadas (`python manage.py migrate`)
- [ ] Servidor corriendo (`python manage.py runserver`)
- [ ] API accesible en `http://127.0.0.1:8000/api/markers/`
- [ ] CORS configurado correctamente
- [ ] Panel admin accesible (opcional)

---

<div align="center">

**Backend listo para usar! 🎉**

Desarrollado con Django + Django REST Framework

</div>

