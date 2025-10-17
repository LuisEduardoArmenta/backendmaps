# ✅ Código ya subido a GitHub

Tu backend ya está en: https://github.com/LuisEduardoArmenta/backendmaps

---

## 🚀 Próximos pasos para desplegar en Railway

### 1️⃣ Ir a Railway

1. Ve a [railway.app](https://railway.app)
2. Haz clic en **"Login"** o **"Start a New Project"**
3. Inicia sesión con **GitHub**

### 2️⃣ Crear proyecto desde tu repositorio

1. Haz clic en **"New Project"**
2. Selecciona **"Deploy from GitHub repo"**
3. Autoriza a Railway (si es tu primera vez)
4. Busca y selecciona **`backendmaps`**
5. Railway empezará a desplegar automáticamente

### 3️⃣ Configurar variables de entorno

Mientras se despliega, configura las variables:

1. Haz clic en tu proyecto en Railway
2. Ve a **"Variables"** (o Settings → Variables)
3. Haz clic en **"+ New Variable"** para cada una:

#### Variables de MySQL (Hostinger)

```
MYSQL_DATABASE=u739395885_map
MYSQL_USER=u739395885_ltx
MYSQL_PASSWORD=mF5vpmgmv7bfVrM.19
MYSQL_HOST=auth-db1026.hstgr.io
MYSQL_PORT=3306
```

#### Variables de Django

```
SECRET_KEY=django-insecure-p9x2m4k7n8q1w5e6r3t9y0u8i7o6p5a4s3d2f1g0h
DEBUG=False
ALLOWED_HOSTS=*.railway.app
```

### 4️⃣ Habilitar MySQL Remoto en Hostinger

**⚠️ SUPER IMPORTANTE** - Sin esto, Railway NO podrá conectarse:

1. Ve al panel de Hostinger
2. **Bases de datos** → Selecciona `u739395885_map`
3. Busca **"MySQL Remoto"** o **"Remote MySQL"**
4. **Habilita** el acceso remoto
5. En "Hosts permitidos", agrega: `%` (permite todas las IPs)
   - O mejor: espera a que Railway te dé una IP y agrégala

### 5️⃣ Esperar el deployment

En Railway → **Deployments**, verás:

```
✅ Installing dependencies from requirements.txt
✅ Running migrations (python manage.py migrate)
✅ Collecting static files (collectstatic)
✅ Starting gunicorn server
```

Si todo sale bien, verás: **"Deployment successful"**

### 6️⃣ Obtener tu URL

1. Ve a **Settings** → **Domains**
2. Verás algo como:
   ```
   https://backendmaps-production.up.railway.app
   ```
3. Copia esa URL

### 7️⃣ Probar la API

Abre en tu navegador:
```
https://backendmaps-production.up.railway.app/api/markers/
```

Deberías ver:
- `[]` si no hay marcadores
- O los marcadores que ya tenías en Hostinger

---

## 🔗 Conectar con tu frontend Angular

Actualiza `frontend/project/src/app/services/ubicaciones.ts`:

```typescript
// Cambiar:
private apiUrl = 'http://127.0.0.1:8000/api/markers/';

// Por tu URL de Railway:
private apiUrl = 'https://backendmaps-production.up.railway.app/api/markers/';
```

Luego, cuando despliegues el frontend (en Vercel/Netlify), agrega a Railway:
```
CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app
```

---

## 🐛 Si algo falla

### ❌ Error: "Can't connect to MySQL server"

1. Verifica que hayas habilitado **MySQL Remoto** en Hostinger
2. Agrega `%` a los hosts permitidos
3. Revisa que las variables de MySQL en Railway sean correctas

### ❌ Error: "Application failed to respond"

1. Ve a Railway → **Deployments** → Logs
2. Busca errores en rojo
3. Verifica que todas las variables estén configuradas

### ❌ Error: "DisallowedHost"

1. Agrega `ALLOWED_HOSTS=*.railway.app` en Variables
2. O agrega el dominio específico que Railway te dio

### ❌ Error: "relation does not exist"

Las migraciones no se ejecutaron. Verifica en los logs:
```
Running migrations...
```

---

## ✅ Checklist final

- [x] Código en GitHub ✅
- [ ] Proyecto creado en Railway
- [ ] Variables de MySQL configuradas
- [ ] Variables de Django configuradas
- [ ] MySQL Remoto habilitado en Hostinger
- [ ] Deploy exitoso
- [ ] API responde en `/api/markers/`
- [ ] Frontend actualizado con nueva URL

---

## 📚 Documentación

- **Guía específica MySQL**: [RAILWAY_MYSQL_HOSTINGER.md](./RAILWAY_MYSQL_HOSTINGER.md)
- **Guía rápida**: [RAILWAY_QUICKSTART.md](./RAILWAY_QUICKSTART.md)
- **Guía completa**: [RAILWAY_DEPLOY.md](./RAILWAY_DEPLOY.md)

---

## 🎉 ¡A desplegar!

Todo está listo. Solo sigue los 7 pasos de arriba y en 10 minutos tendrás tu backend en la nube.

**Repositorio:** https://github.com/LuisEduardoArmenta/backendmaps
**Próximo paso:** Ir a railway.app y crear el proyecto

