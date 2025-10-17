# 📁 Archivos para Railway - Resumen

## ✅ Archivos creados/modificados para Railway

### 🔧 Archivos de configuración

| Archivo | Propósito | Obligatorio |
|---------|-----------|-------------|
| `requirements.txt` | Lista de dependencias Python | ✅ Sí |
| `Procfile` | Comando para iniciar la aplicación | ✅ Sí |
| `railway.json` | Configuración de build y deploy | ⚠️ Recomendado |
| `runtime.txt` | Versión de Python a usar | ⚠️ Recomendado |
| `settings.py` | Configuración de Django (modificado) | ✅ Sí |

---

## 📄 Detalle de cada archivo

### 1. `requirements.txt`
```
asgiref==3.10.0
Django==5.2.7
django-cors-headers==4.9.0
django-filter==25.2
djangorestframework==3.16.1
mysqlclient==2.2.7
sqlparse==0.5.3
tzdata==2025.2

# Para Railway (producción)
gunicorn==23.0.0           # ← Servidor WSGI para producción
psycopg2-binary==2.9.10    # ← Conector de PostgreSQL
whitenoise==6.8.2          # ← Para servir archivos estáticos
dj-database-url==2.3.0     # ← Para parsear DATABASE_URL
```

**¿Qué hace?**
- Lista todas las dependencias que Railway debe instalar
- `gunicorn`: Servidor web para producción (mejor que runserver)
- `psycopg2-binary`: Permite conectar a PostgreSQL de Railway
- `whitenoise`: Sirve archivos estáticos sin nginx
- `dj-database-url`: Facilita la configuración de la base de datos

---

### 2. `Procfile`
```
web: gunicorn maps_backend.wsgi --log-file -
```

**¿Qué hace?**
- Define el comando que Railway debe ejecutar para iniciar la app
- `web:` indica que es un proceso web (responde a HTTP)
- `gunicorn maps_backend.wsgi` inicia el servidor WSGI
- `--log-file -` envía los logs a stdout (Railway los captura)

---

### 3. `railway.json`
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn maps_backend.wsgi --log-file -",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

**¿Qué hace?**
- **`migrate`**: Ejecuta migraciones de base de datos antes de iniciar
- **`collectstatic`**: Recopila archivos estáticos
- **`gunicorn`**: Inicia el servidor web
- **`restartPolicyType`**: Reinicia automáticamente si falla
- **`restartPolicyMaxRetries`**: Máximo 10 reintentos

---

### 4. `runtime.txt`
```
python-3.12.0
```

**¿Qué hace?**
- Especifica la versión exacta de Python a usar
- Evita problemas de compatibilidad
- Railway usa esta versión en el build

---

### 5. `settings.py` (modificado)

#### 5.1 Variables de entorno
```python
import os
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-key')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')
```

**¿Qué hace?**
- Lee configuración desde variables de entorno
- Usa valores por defecto en desarrollo
- En Railway, usa las variables configuradas

#### 5.2 Base de datos flexible
```python
DATABASE_URL = os.environ.get('DATABASE_URL')

if DATABASE_URL:
    # Producción: PostgreSQL de Railway
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
        )
    }
else:
    # Desarrollo: SQLite local
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

**¿Qué hace?**
- Si existe `DATABASE_URL` (Railway), usa PostgreSQL
- Si no (desarrollo local), usa SQLite
- `conn_max_age=600`: Mantiene conexiones por 10 minutos

#### 5.3 WhiteNoise para archivos estáticos
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # ← Agregado
    ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

**¿Qué hace?**
- WhiteNoise sirve archivos estáticos directamente
- No necesitas nginx o Apache
- Comprime archivos automáticamente

#### 5.4 CORS flexible
```python
CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', 
    'http://localhost:4200,http://127.0.0.1:4200'
).split(',')

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CORS_ALLOW_ALL_ORIGINS = False
```

**¿Qué hace?**
- En desarrollo: permite todos los orígenes
- En producción: solo permite orígenes específicos
- Configurable vía variable de entorno

---

## 🔐 Variables de entorno en Railway

Configura estas en **Railway → Variables**:

| Variable | Ejemplo | Descripción |
|----------|---------|-------------|
| `SECRET_KEY` | `django-secret-abc123...` | Clave secreta de Django |
| `DEBUG` | `False` | Desactivar modo debug |
| `ALLOWED_HOSTS` | `*.railway.app` | Hosts permitidos |
| `CORS_ALLOWED_ORIGINS` | `https://mi-frontend.com` | Orígenes CORS permitidos |
| `DATABASE_URL` | *(automático)* | Railway lo configura solo |

---

## 🚀 Flujo de deployment

1. **Build** (automático):
   ```bash
   pip install -r requirements.txt
   ```

2. **Deploy** (definido en `railway.json`):
   ```bash
   python manage.py migrate           # Crea/actualiza tablas
   python manage.py collectstatic     # Recopila archivos estáticos
   gunicorn maps_backend.wsgi         # Inicia servidor web
   ```

3. **Railway asigna**:
   - URL pública (ej: `https://tu-app.railway.app`)
   - Puerto automático (via variable `PORT`)
   - Certificado SSL/HTTPS automático

---

## ✅ Checklist antes de deploy

- [ ] `requirements.txt` tiene todas las dependencias
- [ ] `Procfile` apunta a tu proyecto (`maps_backend.wsgi`)
- [ ] `railway.json` tiene el comando de migrate
- [ ] `settings.py` lee variables de entorno
- [ ] `.gitignore` excluye `venv/`, `.env`, `db.sqlite3`
- [ ] Código está en GitHub
- [ ] PostgreSQL agregado en Railway
- [ ] Variables de entorno configuradas

---

## 📚 Archivos de documentación

| Archivo | Contenido |
|---------|-----------|
| `RAILWAY_QUICKSTART.md` | Guía rápida (5 minutos) |
| `RAILWAY_DEPLOY.md` | Guía completa paso a paso |
| `RAILWAY_FILES.md` | Este archivo (explicación de archivos) |
| `railway.env.example` | Ejemplo de variables de entorno |

---

## 🎯 Resultado final

Después del deploy, tendrás:

```
✅ Backend Django corriendo en Railway
✅ PostgreSQL en la nube
✅ HTTPS automático
✅ Deploy automático desde GitHub
✅ Migraciones automáticas en cada deploy
✅ Archivos estáticos servidos con WhiteNoise
✅ CORS configurado para tu frontend
✅ Variables de entorno seguras

URL de tu API:
https://tu-app-production.up.railway.app/api/markers/
```

---

## 🆘 Troubleshooting rápido

### ❌ Error: "Application failed to respond"
- Verifica que `Procfile` existe y apunta a `maps_backend.wsgi`
- Revisa los logs en Railway

### ❌ Error: "No module named 'gunicorn'"
- Asegúrate de que `gunicorn` está en `requirements.txt`
- Haz `git push` para redeployar

### ❌ Error: "DisallowedHost"
- Configura `ALLOWED_HOSTS=*.railway.app` en Variables

### ❌ Error: "relation does not exist"
- Las migraciones no se ejecutaron
- Verifica que `railway.json` tiene `python manage.py migrate`

---

## 📞 Recursos

- [Railway Docs](https://docs.railway.app/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Gunicorn Docs](https://docs.gunicorn.org/)

