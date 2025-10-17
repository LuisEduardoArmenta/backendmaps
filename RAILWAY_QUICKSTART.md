# ⚡ Railway - Inicio Rápido (5 minutos)

## 🎯 Pasos mínimos para desplegar

### 1️⃣ Subir a GitHub
```bash
cd backend
git init
git add .
git commit -m "Backend listo para Railway"
git remote add origin https://github.com/TU_USUARIO/maps-backend.git
git push -u origin main
```

### 2️⃣ Crear proyecto en Railway
1. Ve a [railway.app](https://railway.app)
2. Login con GitHub
3. **"New Project"** → **"Deploy from GitHub repo"**
4. Selecciona tu repositorio

### 3️⃣ Agregar PostgreSQL
1. En tu proyecto: **"+ New"** → **"Database"** → **"PostgreSQL"**
2. Railway conectará automáticamente `DATABASE_URL`

### 4️⃣ Configurar variables
En **Variables**, agrega:
```
SECRET_KEY=django-insecure-ABC123XYZ789
DEBUG=False
ALLOWED_HOSTS=*.railway.app
```

### 5️⃣ ¡Listo! 🎉
Railway desplegará automáticamente. En ~3 minutos verás tu URL:
```
https://tu-app-production.up.railway.app/api/markers/
```

---

## 🔗 Conectar con frontend

Actualiza `frontend/project/src/app/services/ubicaciones.ts`:
```typescript
private apiUrl = 'https://tu-app-production.up.railway.app/api/markers/';
```

Y agrega la URL de tu frontend a las variables de Railway:
```
CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app
```

---

## ✅ Archivos necesarios (ya incluidos)

- ✅ `requirements.txt` - Dependencias
- ✅ `Procfile` - Comando de inicio
- ✅ `railway.json` - Configuración de build
- ✅ `runtime.txt` - Versión de Python
- ✅ `settings.py` - Ya configurado para Railway

---

## 📖 Documentación completa
Ver [RAILWAY_DEPLOY.md](./RAILWAY_DEPLOY.md) para la guía detallada.

