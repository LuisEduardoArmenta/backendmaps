# 🚀 Guía de Despliegue en Railway

Esta guía te ayudará a desplegar tu backend Django en Railway paso a paso.

---

## ✅ Pre-requisitos

1. ✅ Cuenta en [Railway.app](https://railway.app) (gratis)
2. ✅ Cuenta en GitHub
3. ✅ Tu proyecto subido a GitHub

---

## 📦 Paso 1: Preparar el repositorio en GitHub

### 1.1 Inicializar Git (si no lo has hecho)

```bash
cd backend
git init
git add .
git commit -m "Initial commit - Backend para Railway"
```

### 1.2 Crear repositorio en GitHub

1. Ve a [GitHub](https://github.com) y crea un nuevo repositorio
2. Nómbralo como quieras (ej: `maps-backend`)
3. **NO inicialices** con README, .gitignore ni licencia

### 1.3 Subir código a GitHub

```bash
git remote add origin https://github.com/TU_USUARIO/maps-backend.git
git branch -M main
git push -u origin main
```

---

## 🚂 Paso 2: Crear proyecto en Railway

### 2.1 Ingresar a Railway

1. Ve a [railway.app](https://railway.app)
2. Haz clic en **"Login"** o **"Start a New Project"**
3. Inicia sesión con GitHub

### 2.2 Crear nuevo proyecto

1. Haz clic en **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Autoriza a Railway para acceder a tus repositorios
4. Selecciona tu repositorio `maps-backend`

---

## 🗄️ Paso 3: Agregar base de datos PostgreSQL

Railway detectará automáticamente que es un proyecto Django.

### 3.1 Agregar PostgreSQL

1. En tu proyecto de Railway, haz clic en **"+ New"**
2. Selecciona **"Database"**
3. Elige **"PostgreSQL"**
4. Railway creará automáticamente la base de datos

### 3.2 Conectar PostgreSQL al servicio

Railway agregará automáticamente la variable `DATABASE_URL` a tu servicio. **No necesitas hacer nada más**.

---

## ⚙️ Paso 4: Configurar variables de entorno

### 4.1 Ir a Variables

1. En tu proyecto de Railway, haz clic en tu servicio (no en la DB)
2. Ve a la pestaña **"Variables"**

### 4.2 Agregar variables necesarias

Haz clic en **"+ Add Variable"** y agrega las siguientes:

| Variable | Valor | Descripción |
|----------|-------|-------------|
| `SECRET_KEY` | `tu-clave-super-secreta-123` | Genera una clave segura |
| `DEBUG` | `False` | Desactivar modo debug |
| `ALLOWED_HOSTS` | `*.railway.app` | Dominios permitidos |

**✅ Ejemplo de SECRET_KEY seguro:**
```
django-insecure-@k9m2!p#x8$w5&n7q^v*z1c4d6f8g0h2j4k6m8n0p2q4r6s8t0u2v4
```

### 4.3 Variables automáticas

Railway configurará automáticamente:
- ✅ `DATABASE_URL` (cuando agregues PostgreSQL)
- ✅ `PORT` (Railway asigna el puerto)
- ✅ `RAILWAY_ENVIRONMENT` (production)

---

## 🚀 Paso 5: Deploy automático

### 5.1 Railway desplegará automáticamente

Railway detectará:
- ✅ `requirements.txt` - instalará dependencias
- ✅ `Procfile` - ejecutará gunicorn
- ✅ `railway.json` - ejecutará migraciones y collectstatic

### 5.2 Ver logs

1. Ve a la pestaña **"Deployments"**
2. Haz clic en el deployment activo
3. Verás los logs en tiempo real

**Busca estas líneas para confirmar éxito:**
```
✅ Installing dependencies...
✅ Running migrations...
✅ Collecting static files...
✅ Starting gunicorn...
```

### 5.3 Ver URL de tu API

1. Ve a la pestaña **"Settings"**
2. En la sección **"Domains"**, verás tu URL:
   ```
   https://tu-app-production.up.railway.app
   ```

---

## 🧪 Paso 6: Probar la API

### 6.1 Probar endpoint de marcadores

Abre en tu navegador o Postman:

```
https://tu-app-production.up.railway.app/api/markers/
```

**✅ Deberías ver:**
```json
[]
```

### 6.2 Crear un marcador de prueba

Usa Postman o curl:

```bash
curl -X POST https://tu-app-production.up.railway.app/api/markers/ \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Test Railway",
    "categoria": "Prueba",
    "direccion": "Dirección de prueba",
    "lat": "19.058224",
    "lng": "-98.223395"
  }'
```

**✅ Deberías recibir:**
```json
{
  "id": 1,
  "nombre": "Test Railway",
  "categoria": "Prueba",
  "direccion": "Dirección de prueba",
  "lat": "19.058224000",
  "lng": "-98.223395000",
  "created_at": "2024-10-17T12:00:00Z",
  "updated_at": "2024-10-17T12:00:00Z"
}
```

---

## 🔗 Paso 7: Conectar con tu frontend

### 7.1 Actualizar URL del backend en Angular

En `frontend/project/src/app/services/ubicaciones.ts`:

```typescript
// Cambiar:
private apiUrl = 'http://127.0.0.1:8000/api/markers/';

// Por:
private apiUrl = 'https://tu-app-production.up.railway.app/api/markers/';
```

### 7.2 Actualizar CORS en Railway

1. Ve a Railway → Variables
2. Agrega o actualiza `CORS_ALLOWED_ORIGINS`:
   ```
   https://tu-frontend.vercel.app,https://tu-frontend.netlify.app
   ```

---

## 🔄 Paso 8: Deploys automáticos

### 8.1 Deploy automático con Git

Cada vez que hagas `git push` a tu rama `main`, Railway desplegará automáticamente:

```bash
git add .
git commit -m "Actualización del backend"
git push origin main
```

Railway detectará el push y redesplegará en ~2 minutos.

### 8.2 Ver historial de deploys

En Railway → **Deployments** verás todos tus deploys anteriores.

---

## 🐛 Troubleshooting

### Error: "Application failed to respond"

**Causa:** Gunicorn no está iniciando correctamente.

**Solución:**
1. Verifica que `Procfile` existe
2. Verifica que `gunicorn` está en `requirements.txt`
3. Revisa los logs en Railway

### Error: "No module named 'psycopg2'"

**Causa:** Falta `psycopg2-binary` en requirements.txt.

**Solución:**
```bash
echo "psycopg2-binary==2.9.10" >> requirements.txt
git add requirements.txt
git commit -m "Add psycopg2-binary"
git push
```

### Error: "DisallowedHost at /"

**Causa:** `ALLOWED_HOSTS` no incluye el dominio de Railway.

**Solución:**
1. Ve a Railway → Variables
2. Actualiza `ALLOWED_HOSTS`:
   ```
   *.railway.app,tu-app-production.up.railway.app
   ```

### Error: "relation does not exist"

**Causa:** Las migraciones no se ejecutaron.

**Solución:**
1. Revisa los logs
2. Busca errores en la sección de migraciones
3. Asegúrate de que `railway.json` tiene el comando de migración

### Base de datos vacía después de deploy

**Causa:** Normal, PostgreSQL de Railway está vacía inicialmente.

**Solución:**
- La base de datos estará vacía al inicio
- Los marcadores que tenías en SQLite local NO se migran automáticamente
- Crea nuevos marcadores desde el frontend

---

## 🎯 Comandos útiles en Railway

### Ver logs en tiempo real

Railway CLI (opcional):
```bash
railway logs
```

### Ejecutar comandos en el servidor

```bash
railway run python manage.py createsuperuser
```

---

## 📊 Monitoreo

### Ver métricas

En Railway → **Metrics** verás:
- CPU usage
- Memory usage
- Network traffic
- Request count

---

## 💰 Costos

### Plan gratuito de Railway

- ✅ $5 USD de crédito gratis al mes
- ✅ Suficiente para desarrollo y proyectos pequeños
- ✅ PostgreSQL incluido
- ✅ Deploy ilimitados

### Cuándo necesitas pagar

Si tu app recibe mucho tráfico, Railway cobrará según uso:
- CPU: ~$0.000463/min
- RAM: ~$0.000231/GB/min
- Network: ~$0.10/GB

**Para un proyecto pequeño, el plan gratuito es suficiente.**

---

## ✅ Checklist de deployment

- [ ] Código subido a GitHub
- [ ] Proyecto creado en Railway
- [ ] PostgreSQL agregado
- [ ] Variables de entorno configuradas
- [ ] Deploy exitoso (logs sin errores)
- [ ] API responde en `/api/markers/`
- [ ] Frontend actualizado con nueva URL
- [ ] CORS configurado correctamente

---

## 🎉 ¡Listo!

Tu backend Django está desplegado en Railway con:
- ✅ PostgreSQL en la nube
- ✅ HTTPS automático
- ✅ Deploy automático desde GitHub
- ✅ Migraciones automáticas
- ✅ Archivos estáticos servidos con WhiteNoise

**URL de tu API:**
```
https://tu-app-production.up.railway.app/api/markers/
```

---

## 📚 Recursos adicionales

- [Documentación de Railway](https://docs.railway.app/)
- [Guía de Django en Railway](https://docs.railway.app/guides/django)
- [Railway CLI](https://docs.railway.app/develop/cli)

---

## 🆘 ¿Necesitas ayuda?

Si tienes problemas:
1. Revisa los logs en Railway
2. Verifica las variables de entorno
3. Asegúrate de que PostgreSQL está conectado
4. Revisa que todas las dependencias estén en `requirements.txt`

