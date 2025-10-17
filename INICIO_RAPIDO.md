# ⚡ Inicio Rápido - Backend Django

Guía super rápida para poner en marcha el backend en 5 minutos.

---

## 🚀 Pasos Rápidos

### 1️⃣ Configurar MySQL (2 minutos)

Edita `maps_backend/settings.py`, busca `DATABASES` y reemplaza:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'TU_BASE_DE_DATOS',      # ⬅️ Cambiar
        'USER': 'TU_USUARIO',             # ⬅️ Cambiar
        'PASSWORD': 'TU_CONTRASEÑA',      # ⬅️ Cambiar
        'HOST': 'TU_HOST',                # ⬅️ Cambiar (ej: srv1234.hostinger.com)
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
        },
    }
}
```

### 2️⃣ Activar Virtual Environment (30 segundos)

```bash
cd backend
.\venv\Scripts\Activate.ps1
```

### 3️⃣ Ejecutar Migraciones (1 minuto)

```bash
python manage.py migrate
```

### 4️⃣ Ejecutar el Servidor (10 segundos)

```bash
python manage.py runserver
```

---

## ✅ Verificar que Funciona

### Prueba 1: API Root

Abre en tu navegador:
```
http://127.0.0.1:8000
```

Deberías ver un JSON con información de la API.

### Prueba 2: Lista de Marcadores

```
http://127.0.0.1:8000/api/markers/
```

Deberías ver la interfaz navegable de Django REST Framework.

### Prueba 3: Crear un Marcador

En la interfaz web de DRF, llena el formulario:

```
nombre: Test Café
categoria: Cafetería
direccion: Av. Test 123
lat: 19.0433
lng: -98.2019
```

Haz clic en "POST" y deberías ver:

```json
{
  "message": "Marcador creado exitosamente",
  "data": {
    "id": 1,
    "nombre": "Test Café",
    ...
  }
}
```

---

## 🎯 Endpoints Disponibles

```
GET    http://127.0.0.1:8000/api/markers/          → Listar
POST   http://127.0.0.1:8000/api/markers/          → Crear
GET    http://127.0.0.1:8000/api/markers/1/        → Ver detalle
PUT    http://127.0.0.1:8000/api/markers/1/        → Actualizar
DELETE http://127.0.0.1:8000/api/markers/1/        → Eliminar
GET    http://127.0.0.1:8000/api/markers/stats/    → Estadísticas
```

---

## 🔧 (Opcional) Crear Superusuario

Para acceder al panel de administración:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones y luego accede:

```
http://127.0.0.1:8000/admin/
```

---

## 🐛 Problemas Comunes

### Error: "Unknown server host"

**Solución:** No configuraste las credenciales de MySQL en `settings.py`

### Error: "No module named 'mysqlclient'"

**Solución:**
```bash
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Error: "Table doesn't exist"

**Solución:** No ejecutaste las migraciones:
```bash
python manage.py migrate
```

### Error: CORS en el frontend

**Solución:** Ya está configurado en `settings.py` con `CORS_ALLOW_ALL_ORIGINS = True`

---

## 📚 Documentación Completa

- **[README.md](./README.md)** - Documentación completa
- **[INTEGRACION_FRONTEND.md](./INTEGRACION_FRONTEND.md)** - Conectar con Angular

---

## ✅ Checklist

- [ ] MySQL configurado en `settings.py`
- [ ] Virtual environment activado
- [ ] Migraciones ejecutadas (`python manage.py migrate`)
- [ ] Servidor corriendo (`python manage.py runserver`)
- [ ] API accesible en `http://127.0.0.1:8000/api/markers/`

---

**¡Listo en 5 minutos!** 🎉

Ahora puedes conectar el frontend Angular siguiendo `INTEGRACION_FRONTEND.md`

