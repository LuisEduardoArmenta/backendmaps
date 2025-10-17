# ✅ Código ya en GitHub - Desplegar en Render

**Repositorio:** https://github.com/LuisEduardoArmenta/backendmaps

---

## 🚀 Pasos para desplegar en Render (10 minutos)

### 1️⃣ Crear cuenta en Render

1. Ve a [render.com](https://render.com)
2. Haz clic en **"Get Started"**
3. **Sign up con GitHub** (más fácil)

### 2️⃣ Crear Web Service

1. En Render Dashboard, haz clic en **"New +"**
2. Selecciona **"Web Service"**
3. Autoriza a Render para acceder a GitHub
4. Busca y selecciona **`backendmaps`**
5. Haz clic en **"Connect"**

### 3️⃣ Configurar el servicio

Llena el formulario con estos valores:

| Campo | Valor |
|-------|-------|
| **Name** | `backendmaps` |
| **Region** | `Oregon (US West)` |
| **Branch** | `main` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn maps_backend.wsgi:application` |
| **Instance Type** | `Free` |

### 4️⃣ Agregar variables de entorno

**Baja** hasta la sección **"Environment Variables"** y haz clic en **"Add Environment Variable"** para cada una:

#### MySQL de Hostinger:
```
MYSQL_DATABASE = u739395885_map
MYSQL_USER = u739395885_ltx
MYSQL_PASSWORD = mF5vpmgmv7bfVrM.19
MYSQL_HOST = auth-db1026.hstgr.io
MYSQL_PORT = 3306
```

#### Django:
```
SECRET_KEY = django-insecure-p9x2m4k7n8q1w5e6r3t9y0u8i7o6p5a4s3d2f1g0h
DEBUG = False
ALLOWED_HOSTS = .onrender.com
PYTHON_VERSION = 3.12.0
```

### 5️⃣ Habilitar MySQL Remoto en Hostinger

**⚠️ MUY IMPORTANTE - Sin esto NO funcionará:**

1. Panel de Hostinger → **Bases de datos**
2. Selecciona `u739395885_map`
3. Busca **"MySQL Remoto"**
4. **Habilita** el acceso remoto
5. Agrega `%` en "Hosts permitidos" (permite todas las IPs)

### 6️⃣ Crear el servicio

1. Haz clic en **"Create Web Service"**
2. Render empezará a desplegar
3. **Espera 3-5 minutos** (la primera vez tarda más)

### 7️⃣ Verificar deployment

En los **Logs** verás:

```
✅ Cloning from GitHub...
✅ Installing dependencies...
✅ Collecting static files...
✅ Running migrations...
✅ Your service is live 🎉
```

### 8️⃣ Obtener tu URL

Tu backend estará en:
```
https://backendmaps.onrender.com
```

Pruébalo abriendo:
```
https://backendmaps.onrender.com/api/markers/
```

---

## 🔗 Conectar con el frontend

Actualiza `frontend/project/src/app/services/ubicaciones.ts`:

```typescript
private apiUrl = 'https://backendmaps.onrender.com/api/markers/';
```

---

## ⚠️ Notas importantes sobre Render Free

### El servicio se "duerme"

- Después de 15 min sin tráfico, Render pone el servicio a dormir
- La primera petición tardará ~30 segundos (se despierta automáticamente)
- Las siguientes peticiones serán normales
- Es normal en el plan Free

### Soluciones:

1. **Para desarrollo:** No importa, es gratis
2. **Para producción:** Actualiza a plan Starter ($7/mes) - siempre activo
3. **Hack gratuito:** Usa un servicio de ping cada 14 min (ej: UptimeRobot)

---

## 🐛 Si algo sale mal

### Error: "Build failed"

1. Ve a **Logs** en Render
2. Busca líneas rojas con error
3. Verifica que `build.sh` tenga permisos:
   ```bash
   chmod +x build.sh
   git add build.sh
   git commit -m "Fix permissions"
   git push
   ```

### Error: "Can't connect to MySQL"

1. Verifica que hayas habilitado **MySQL Remoto** en Hostinger
2. Revisa que las variables de MySQL sean correctas
3. Agrega `%` a los hosts permitidos en Hostinger

### Error: "Application failed to respond"

1. Verifica que `ALLOWED_HOSTS` incluya `.onrender.com`
2. Revisa los logs para ver el error específico

---

## 🔄 Actualizar el backend

Cada vez que hagas cambios:

```bash
git add .
git commit -m "Actualización"
git push origin main
```

Render detectará el push y redesplegará automáticamente en ~2 minutos.

---

## ✅ Checklist

- [ ] Cuenta en Render creada
- [ ] Web Service configurado
- [ ] 10 variables de entorno agregadas
- [ ] MySQL Remoto habilitado en Hostinger
- [ ] Build exitoso (sin errores rojos)
- [ ] URL funcionando: `https://backendmaps.onrender.com/api/markers/`
- [ ] Frontend actualizado con nueva URL

---

## 📚 Guías completas

- **Esta guía rápida:** PASOS_RENDER.md (estás aquí)
- **Guía detallada:** [RENDER_DEPLOY.md](./RENDER_DEPLOY.md)
- **Troubleshooting completo:** [RENDER_DEPLOY.md](./RENDER_DEPLOY.md) (sección de errores)

---

## 🎉 ¡A desplegar!

Todo está listo en GitHub. Solo sigue los 8 pasos de arriba y en 10 minutos tu backend estará en la nube.

**Siguiente:** Ve a [render.com](https://render.com) y crea tu Web Service.

