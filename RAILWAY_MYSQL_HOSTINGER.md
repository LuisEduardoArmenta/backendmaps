# 🚀 Desplegar en Railway con MySQL de Hostinger

Tu backend está configurado para usar **tu base de datos MySQL de Hostinger** desde Railway.

---

## ⚙️ Variables de entorno en Railway

Cuando crees tu proyecto en Railway, configura estas variables en **Settings → Variables**:

### 🔐 Variables obligatorias

| Variable | Valor |
|----------|-------|
| `MYSQL_DATABASE` | `u739395885_map` |
| `MYSQL_USER` | `u739395885_ltx` |
| `MYSQL_PASSWORD` | `mF5vpmgmv7bfVrM.19` |
| `MYSQL_HOST` | `auth-db1026.hstgr.io` |
| `MYSQL_PORT` | `3306` |

### 🔐 Variables de Django

| Variable | Valor recomendado |
|----------|-------------------|
| `SECRET_KEY` | `django-insecure-TU-CLAVE-SUPER-SEGURA-123` |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `*.railway.app` |

### 🌐 Variables de CORS (cuando despliegues el frontend)

| Variable | Valor |
|----------|-------|
| `CORS_ALLOWED_ORIGINS` | `https://tu-frontend.vercel.app` |

---

## ⚠️ IMPORTANTE: Habilitar acceso remoto en Hostinger

Para que Railway pueda conectarse a tu MySQL de Hostinger, debes:

### 1. Permitir conexiones remotas

1. Ve al panel de Hostinger → **Bases de datos**
2. Selecciona tu base de datos `u739395885_map`
3. Busca la sección **"MySQL Remoto"** o **"Remote MySQL"**
4. Habilita el acceso remoto

### 2. Agregar Railway a la whitelist

Railway usa IPs dinámicas, así que tienes 2 opciones:

**Opción A: Permitir todas las IPs (más fácil, menos seguro)**
- Agrega `%` o `0.0.0.0/0` a la whitelist

**Opción B: Usar Railway's static IP (más seguro)**
- Railway te puede asignar una IP estática
- Agrégala a la whitelist de Hostinger

### 3. Verificar puerto 3306

- Asegúrate de que Hostinger permita conexiones en el puerto `3306`
- Algunos proveedores bloquean este puerto por defecto

---

## 🚀 Pasos para desplegar

### 1️⃣ Subir código a GitHub

Ya creaste el repositorio, ahora sube el código:

```bash
cd backend
git add .
git commit -m "Backend configurado para Railway con MySQL"
git push -u origin main
```

### 2️⃣ Crear proyecto en Railway

1. Ve a [railway.app](https://railway.app)
2. Login con GitHub
3. Haz clic en **"New Project"**
4. Selecciona **"Deploy from GitHub repo"**
5. Elige `backendmaps`

### 3️⃣ Configurar variables de entorno

1. En Railway, ve a tu proyecto
2. Haz clic en el servicio (no agregues PostgreSQL)
3. Ve a **"Variables"**
4. Agrega todas las variables de MySQL y Django (ver tabla arriba)

**⚠️ NO agregues PostgreSQL** porque ya tienes MySQL de Hostinger.

### 4️⃣ Deploy automático

Railway desplegará automáticamente. En los logs verás:

```
✅ Installing dependencies...
✅ Running migrations...
✅ Collecting static files...
✅ Starting gunicorn...
```

### 5️⃣ Obtener URL

En Railway → **Settings → Domains**, verás tu URL:
```
https://backendmaps-production.up.railway.app
```

---

## 🧪 Probar la conexión

### Verificar que Railway se conectó a MySQL

Desde Railway CLI o en los logs, busca:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, markers, sessions
Running migrations:
  No migrations to apply.
```

Esto confirma que se conectó correctamente a tu MySQL de Hostinger.

### Probar endpoint

```bash
curl https://backendmaps-production.up.railway.app/api/markers/
```

Deberías ver los marcadores que ya tenías en Hostinger (si los hay).

---

## 🔗 Conectar frontend

Actualiza `frontend/project/src/app/services/ubicaciones.ts`:

```typescript
private apiUrl = 'https://backendmaps-production.up.railway.app/api/markers/';
```

Y agrega tu dominio de frontend a Railway (Variables):
```
CORS_ALLOWED_ORIGINS=https://tu-frontend.vercel.app,https://localhost:4200
```

---

## 🐛 Troubleshooting

### ❌ Error: "Can't connect to MySQL server"

**Causa:** Hostinger está bloqueando la conexión desde Railway.

**Solución:**
1. Habilita **MySQL Remoto** en Hostinger
2. Agrega `%` a la whitelist (o la IP de Railway)
3. Verifica que el puerto 3306 esté abierto

### ❌ Error: "Access denied for user"

**Causa:** Credenciales incorrectas.

**Solución:**
1. Verifica que las variables en Railway sean correctas
2. Prueba las credenciales localmente primero
3. Asegúrate de que el usuario tenga permisos remotos

### ❌ Error: "Unknown MySQL server host"

**Causa:** Host incorrecto.

**Solución:**
- Verifica que `MYSQL_HOST` sea `auth-db1026.hstgr.io`
- NO uses la URL completa de phpMyAdmin

### ❌ Error: "Lost connection to MySQL server during query"

**Causa:** Timeout o firewall.

**Solución:**
1. Aumenta `connect_timeout` en settings.py
2. Verifica que Hostinger no tenga límites de conexiones
3. Considera usar un proxy o túnel

---

## 💡 Ventajas de esta configuración

- ✅ Usas tu BD actual de Hostinger (no pierdes datos)
- ✅ Railway solo ejecuta el backend (sin BD adicional)
- ✅ Deploy automático desde GitHub
- ✅ HTTPS gratis
- ✅ Más barato (no pagas por BD en Railway)

---

## ⚠️ Consideraciones importantes

1. **Latencia**: Railway (EE.UU./Europa) → Hostinger puede tener latencia
2. **Conexiones**: Hostinger puede limitar conexiones simultáneas
3. **Seguridad**: No expongas credenciales en el código (usa variables de entorno)
4. **Backup**: Haz respaldo de tu BD de Hostinger regularmente

---

## 🔄 Alternativa: Migrar a PostgreSQL de Railway (opcional)

Si Hostinger da problemas, puedes migrar a PostgreSQL de Railway:

```bash
# Exportar datos de MySQL
python manage.py dumpdata > backup.json

# Cambiar a PostgreSQL en Railway
# Importar datos
python manage.py loaddata backup.json
```

Pero por ahora, usemos tu MySQL existente.

---

## ✅ Checklist de deployment

- [ ] Código subido a GitHub
- [ ] Proyecto creado en Railway
- [ ] Variables de MySQL configuradas
- [ ] Variables de Django configuradas
- [ ] MySQL Remoto habilitado en Hostinger
- [ ] Railway agregado a whitelist de Hostinger
- [ ] Deploy exitoso (logs sin errores)
- [ ] API responde en `/api/markers/`
- [ ] Datos de Hostinger accesibles

---

## 🎉 ¡Listo!

Tu backend en Railway se conectará a tu MySQL de Hostinger y funcionará perfectamente.

**URL de tu API:**
```
https://backendmaps-production.up.railway.app/api/markers/
```

