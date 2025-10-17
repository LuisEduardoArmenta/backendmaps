# 🚀 Desplegar Backend en Render con MySQL de Hostinger

Tu backend Django está configurado para desplegarse en **Render** usando tu base de datos MySQL de Hostinger.

---

## ✅ Archivos ya configurados

- ✅ `render.yaml` - Configuración de Render
- ✅ `build.sh` - Script de build (migraciones y collectstatic)
- ✅ `requirements.txt` - Dependencias Python
- ✅ `Procfile` - Comando de inicio (gunicorn)
- ✅ `settings.py` - Lee variables de entorno

---

## 🚀 Pasos para desplegar

### 1️⃣ Ir a Render

1. Ve a [render.com](https://render.com)
2. Haz clic en **"Get Started"** o **"Sign Up"**
3. Inicia sesión con **GitHub**

### 2️⃣ Crear Web Service

1. En el dashboard, haz clic en **"New +"**
2. Selecciona **"Web Service"**
3. Conecta tu cuenta de GitHub (si es la primera vez)
4. Busca y selecciona **`backendmaps`**
5. Haz clic en **"Connect"**

### 3️⃣ Configurar el servicio

Render detectará automáticamente que es Python. Configura:

| Campo | Valor |
|-------|-------|
| **Name** | `backendmaps` (o el que prefieras) |
| **Region** | `Oregon (US West)` o el más cercano |
| **Branch** | `main` |
| **Root Directory** | *(dejar vacío)* |
| **Runtime** | `Python 3` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn maps_backend.wsgi:application` |
| **Instance Type** | `Free` (para empezar) |

### 4️⃣ Configurar variables de entorno

Antes de hacer clic en "Create Web Service", **baja hasta "Environment Variables"** y agrega:

#### Variables de MySQL (Hostinger)

| Key | Value |
|-----|-------|
| `MYSQL_DATABASE` | `u739395885_map` |
| `MYSQL_USER` | `u739395885_ltx` |
| `MYSQL_PASSWORD` | `mF5vpmgmv7bfVrM.19` |
| `MYSQL_HOST` | `auth-db1026.hstgr.io` |
| `MYSQL_PORT` | `3306` |

#### Variables de Django

| Key | Value |
|-----|-------|
| `SECRET_KEY` | `django-insecure-TU-CLAVE-SUPER-SEGURA-ABC123XYZ` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `backendmaps.onrender.com` |
| `PYTHON_VERSION` | `3.12.0` |

**💡 Tip:** Genera una SECRET_KEY segura con:
```python
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5️⃣ Habilitar MySQL Remoto en Hostinger

**⚠️ SUPER IMPORTANTE** - Sin esto NO funcionará:

1. Ve al **panel de Hostinger**
2. **Bases de datos** → Selecciona `u739395885_map`
3. Busca **"MySQL Remoto"** o **"Remote MySQL"**
4. **Habilita** el acceso remoto
5. En "Hosts permitidos", agrega:
   - `%` (permite todas las IPs)
   - O específicamente las IPs de Render (ver sección de IPs abajo)

### 6️⃣ Crear Web Service

1. Haz clic en **"Create Web Service"**
2. Render empezará a desplegar automáticamente
3. Verás los logs en tiempo real

### 7️⃣ Esperar el deployment

En los logs verás:

```bash
==> Building...
==> Cloning from GitHub...
==> Running build command: ./build.sh
==> Installing dependencies...
==> Collecting static files...
==> Running migrations...
==> Build successful!

==> Starting service...
==> gunicorn maps_backend.wsgi:application
==> Your service is live 🎉
```

### 8️⃣ Obtener tu URL

Una vez desplegado, tu URL será:
```
https://backendmaps.onrender.com
```

O el nombre que hayas elegido.

---

## 🧪 Probar la API

Abre en tu navegador:
```
https://backendmaps.onrender.com/api/markers/
```

Deberías ver:
- `[]` si no hay marcadores
- Los marcadores existentes en tu BD de Hostinger

---

## 🔗 Conectar con tu frontend Angular

Actualiza `frontend/project/src/app/services/ubicaciones.ts`:

```typescript
// Cambiar:
private apiUrl = 'http://127.0.0.1:8000/api/markers/';

// Por:
private apiUrl = 'https://backendmaps.onrender.com/api/markers/';
```

Cuando despliegues el frontend, actualiza la variable CORS en Render:
```
CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app,http://localhost:4200
```

---

## 📌 IPs de Render (para whitelist de Hostinger)

Si Hostinger te pide IPs específicas, Render usa estas:

**Región US West (Oregon):**
```
44.224.0.0/12
52.24.0.0/14
54.68.0.0/14
```

**Región US East (Ohio):**
```
3.128.0.0/14
3.16.0.0/14
```

**Región Europe (Frankfurt):**
```
3.64.0.0/14
3.120.0.0/14
```

Pero es más fácil usar `%` para permitir todas.

---

## 🐛 Troubleshooting

### ❌ Error: "Can't connect to MySQL server"

**Causa:** Hostinger está bloqueando la conexión.

**Solución:**
1. Habilita **MySQL Remoto** en Hostinger
2. Agrega `%` o las IPs de Render a la whitelist
3. Verifica que el puerto 3306 esté abierto

### ❌ Error: "Application Error"

**Causa:** Error en el build o variables mal configuradas.

**Solución:**
1. Ve a **Logs** en Render
2. Busca el error específico
3. Verifica que todas las variables de entorno estén bien

### ❌ Error: "DisallowedHost"

**Causa:** El dominio no está en ALLOWED_HOSTS.

**Solución:**
1. Actualiza `ALLOWED_HOSTS` en Render:
   ```
   ALLOWED_HOSTS=backendmaps.onrender.com,.onrender.com
   ```

### ❌ Error: "relation does not exist"

**Causa:** Las migraciones no se ejecutaron.

**Solución:**
1. Verifica que `build.sh` tenga permisos:
   ```bash
   chmod +x build.sh
   git add build.sh
   git commit -m "Add execute permission to build.sh"
   git push
   ```

### ❌ Error: "ModuleNotFoundError"

**Causa:** Falta una dependencia en requirements.txt.

**Solución:**
- Verifica que todas las dependencias estén listadas
- Agrega la que falta y haz push

---

## 💡 Características de Render

### Plan Free

- ✅ 750 horas/mes gratis
- ✅ Deploy automático desde GitHub
- ✅ HTTPS automático
- ✅ Logs en tiempo real
- ⚠️ Se duerme después de 15 min sin uso (tarda ~30s en despertar)

### Limitaciones Free Tier

- El servicio se "duerme" si no recibe tráfico
- 512 MB de RAM
- Menor CPU que planes pagos
- Perfecto para desarrollo y proyectos pequeños

### Despertar servicio dormido

Si tu servicio se durmió:
1. Solo haz una petición (ej: abre la URL)
2. Esperará ~30 segundos
3. Se activará automáticamente

---

## 🔄 Deploy automático

Cada vez que hagas `git push` a `main`, Render redesplegará automáticamente:

```bash
git add .
git commit -m "Actualización del backend"
git push origin main
```

Render detectará el push y empezará el build en ~30 segundos.

---

## ⚙️ Comandos útiles en Render

### Ver logs

En Render → Tu servicio → **Logs**

### Shell interactivo

En Render → Tu servicio → **Shell**

```bash
python manage.py shell
```

### Ejecutar migraciones manualmente

Si necesitas ejecutar migraciones después del deploy:

1. Ve a **Shell** en Render
2. Ejecuta:
   ```bash
   python manage.py migrate
   ```

### Crear superusuario

En **Shell**:
```bash
python manage.py createsuperuser
```

---

## 🔐 Seguridad

### Variables sensibles

- ✅ `SECRET_KEY` - Genera una única en Render
- ✅ `MYSQL_PASSWORD` - Nunca la subas a GitHub
- ✅ Todas las credenciales en variables de entorno

### ALLOWED_HOSTS

Para producción, especifica dominios exactos:
```
ALLOWED_HOSTS=backendmaps.onrender.com,api.tudominio.com
```

### CORS

Solo permite orígenes conocidos:
```
CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app,https://tu-app.netlify.app
```

---

## 📊 Monitoreo

### Metrics

En Render → Tu servicio → **Metrics**, verás:
- CPU usage
- Memory usage
- Request count
- Response times

### Health checks

Render hace health checks automáticos. Si tu app falla 3 veces, reiniciará.

---

## 💰 Costos

### Free Tier (Actual)

- ✅ 750 horas/mes gratis
- ✅ Suficiente para 1 servicio 24/7
- ✅ Ideal para desarrollo

### Si necesitas más

- **Starter:** $7/mes - Siempre activo, más RAM
- **Standard:** $25/mes - Más CPU y RAM
- **Pro:** $85/mes - Alta performance

Para tu proyecto, **Free es suficiente**.

---

## ✅ Checklist de deployment

- [x] Código en GitHub ✅
- [ ] Cuenta en Render creada
- [ ] Web Service creado
- [ ] Variables de MySQL configuradas
- [ ] Variables de Django configuradas
- [ ] MySQL Remoto habilitado en Hostinger
- [ ] Build exitoso
- [ ] Migraciones ejecutadas
- [ ] API responde en `/api/markers/`
- [ ] Frontend actualizado con nueva URL

---

## 🎉 ¡Listo!

Tu backend Django estará en:
```
https://backendmaps.onrender.com/api/markers/
```

Conectado a tu MySQL de Hostinger, con HTTPS automático y deploy continuo desde GitHub.

---

## 📚 Recursos

- [Documentación Render](https://render.com/docs)
- [Django en Render](https://render.com/docs/deploy-django)
- [Render Dashboard](https://dashboard.render.com/)
- [Soporte Render](https://render.com/support)

---

**¡Tu backend está listo para Render! 🚀**

