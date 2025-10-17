# 🎉 Backend configurado para Render

## ✅ Todo listo en GitHub

**Repositorio:** https://github.com/LuisEduardoArmenta/backendmaps

---

## 📁 Archivos creados para Render

| Archivo | Propósito |
|---------|-----------|
| `render.yaml` | Configuración de Render (auto-detecta el servicio) |
| `build.sh` | Script que ejecuta migraciones y collectstatic |
| `requirements.txt` | Dependencias Python (con gunicorn, mysqlclient, etc.) |
| `Procfile` | Comando de inicio (gunicorn) |
| `settings.py` | Configurado para leer variables de entorno MySQL |

---

## 🚀 SIGUIENTE PASO: Desplegar en Render

### 📖 Lee esta guía paso a paso:

👉 **[PASOS_RENDER.md](./PASOS_RENDER.md)** 👈

Te llevará de la mano en 8 pasos simples (10 minutos).

### O si prefieres la guía completa:

📚 **[RENDER_DEPLOY.md](./RENDER_DEPLOY.md)** - Guía detallada con troubleshooting

---

## ⚡ Resumen rápido

### 1. Ir a Render
- [render.com](https://render.com) → Sign up con GitHub

### 2. Crear Web Service
- New + → Web Service → Selecciona `backendmaps`

### 3. Configurar
- Build Command: `./build.sh`
- Start Command: `gunicorn maps_backend.wsgi:application`
- Instance Type: `Free`

### 4. Variables de entorno (10 variables)

**MySQL (Hostinger):**
```
MYSQL_DATABASE=u739395885_map
MYSQL_USER=u739395885_ltx
MYSQL_PASSWORD=mF5vpmgmv7bfVrM.19
MYSQL_HOST=auth-db1026.hstgr.io
MYSQL_PORT=3306
```

**Django:**
```
SECRET_KEY=django-insecure-TU-CLAVE-SEGURA-123
DEBUG=False
ALLOWED_HOSTS=.onrender.com
PYTHON_VERSION=3.12.0
```

### 5. ⚠️ Habilitar MySQL Remoto en Hostinger
**MUY IMPORTANTE:** Panel Hostinger → Bases de datos → MySQL Remoto → Habilitar → Agregar `%`

### 6. Deploy
Haz clic en "Create Web Service" y espera 3-5 minutos.

---

## 🎯 Resultado

Tu backend estará en:
```
https://backendmaps.onrender.com/api/markers/
```

---

## 🔗 Conectar con frontend

Actualiza `frontend/project/src/app/services/ubicaciones.ts`:

```typescript
private apiUrl = 'https://backendmaps.onrender.com/api/markers/';
```

---

## 💡 Diferencias entre Render y Railway

### ✅ Ventajas de Render

- Más estable para plan gratuito
- Interfaz más simple
- Mejor documentación en español
- Deploy más rápido

### ⚠️ Limitación del plan Free

- Se duerme después de 15 min sin uso
- Primera petición tarda ~30s (se despierta)
- Siguientes peticiones son normales
- **Solución:** Plan Starter $7/mes (siempre activo)

---

## 📚 Documentación

1. **PASOS_RENDER.md** - 🎯 Lee este primero (guía rápida)
2. **RENDER_DEPLOY.md** - Guía completa con troubleshooting
3. **render.yaml** - Configuración del servicio
4. **build.sh** - Script de build

---

## ✅ Checklist

- [x] Código en GitHub ✅
- [x] Archivos de Render creados ✅
- [ ] Cuenta en Render
- [ ] Web Service creado
- [ ] Variables de entorno configuradas
- [ ] MySQL Remoto habilitado en Hostinger
- [ ] Deploy exitoso
- [ ] API funcionando
- [ ] Frontend conectado

---

## 🆘 ¿Problemas?

Consulta la sección **Troubleshooting** en [RENDER_DEPLOY.md](./RENDER_DEPLOY.md)

Errores comunes:
- **Build failed** → Verifica permisos de `build.sh`
- **Can't connect to MySQL** → Habilita MySQL Remoto en Hostinger
- **DisallowedHost** → Agrega `.onrender.com` a `ALLOWED_HOSTS`

---

## 🎉 ¡A desplegar!

**Siguiente paso:** Abre [PASOS_RENDER.md](./PASOS_RENDER.md) y sigue las instrucciones.

Todo está listo. En 10 minutos tu backend estará en la nube. 🚀

